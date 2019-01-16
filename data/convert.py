import os
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

#raw labels
raw_labels = pd.read_csv("train_labels.csv",header=None)[1:].values

with open("train_only.csv","w") as f:
    for value in raw_labels:
        filename = os.getcwd() + "/images/train/"  +value[0]
        if isinstance(value[1],float):
            label = ",,,,"
        else:
            label = value[1].replace(" ",",") + ",gangjin"
        f.write(filename+","+label + "\n")
