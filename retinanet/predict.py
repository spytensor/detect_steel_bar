import numpy as np
import torchvision
import time
import os
import copy
import pdb
import time
import argparse

import sys
import cv2
import skimage
import torch
from torch.utils.data import Dataset, DataLoader
from torchvision import datasets, models, transforms
from IPython import embed
from dataloader import CocoDataset, CSVDataset, collater, Resizer, AspectRatioBasedSampler, Augmenter, UnNormalizer, Normalizer
from torchvision import transforms as T
from glob import glob
assert torch.__version__.split('.')[1] == '4'

print('CUDA available: {}'.format(torch.cuda.is_available()))

# threshold for class score
threshold = 0.5
results_file = open("./submit/larger%s.csv"%str(threshold),"w")

if not os.path.exists("./submit/"):
    os.mkdir("./submit/")

if not os.path.exists("./outputs/"):
    os.mkdir("./outputs/")
if not os.path.exists("./best_models/"):
    os.mkdir("./best_models/")

def demo(image_lists):
    classes = ["gangjin"]
    model = "./best_models/model.pt"
    retinanet = torch.load(model)
    retinanet = retinanet.cuda()
    retinanet.eval()
    #detect
    transforms = T.Compose([
        Normalizer(),
        Resizer()
        ])
    for filename in image_lists:
        image = skimage.io.imread(filename)
        sampler = {"img":image.astype(np.float32)/255.0,"annot":np.empty(shape=(5,5))}
        image_tf = transforms(sampler)
        scale = image_tf["scale"]
        new_shape = image_tf['img'].shape
        x = torch.autograd.Variable(image_tf['img'].unsqueeze(0).transpose(1,3), volatile=True)
        with torch.no_grad():
            scores,_,bboxes = retinanet(x.cuda().float())
            bboxes /= scale
            scores = scores.cpu().data.numpy()
            bboxes = bboxes.cpu().data.numpy()
            # select threshold
            idxs = np.where(scores > threshold)[0]
            scores = scores[idxs]
            bboxes = bboxes[idxs]
            #embed()
            for i,box in enumerate(bboxes):
                 cv2.rectangle(image,(int(box[1]),int(box[0])),(int(box[3]),int(box[2])),color=(0,0,255),thickness=2 )
                 results_file.write(filename.split("/")[-1] +","+ str(int(box[1])) + " " + str(int(box[0])) +  " " + str(int(box[3])) + " " +str(int(box[2])) + "\n")
            print("Predicting image: %s "%filename)
            cv2.imwrite("./outputs/%s"%filename.split("/")[-1],image)
if __name__ == "__main__":
    root = "./data/images/test/"
    image_lists = glob(root+"*.jpg")
    demo(image_lists)
