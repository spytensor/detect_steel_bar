## 提醒

由于个人版本修改较多，记不清哪个配置可以达到线上0.97。

## 声明

由于竞赛平台协议有规定，未经许可暂不能公开数据集，非常抱歉。

可修改的地方:

1. dataloader.py 中Resize函数的图像尺寸，越大效果越好。
2. main.py 中的模型 depth ，越大效果越好。
3. 更有效的办法就是做数据扩充，增加数据量。

## 1. 比赛地址

[智能盘点—钢筋数量AI识别](https://www.datafountain.cn/competitions/332/details)

## 2. 依赖

`pytorch0.4.1`,`opencv-python`,`skimage`

## 3. 使用方法

step0: 安装

```
git clone https://github.com/spytensor/detect_steel_bar.git
detect_steel_bar/retinanet/lib/
bash build.sh
cd ../../
```

step1: 下载数据解压后，将训练数据和测试数据放到 `data/images/`下，效果如下：
     
     - data/
        - images/
            train/
            test/
 step2: 将训练标签文件 `train_labels.csv` 复制到 `data/` 下，效果如下：
 
    - data/
        train_labels.csv
 step3: 将官方提高数据转变成可供Retinanet训练格式
 ```
 cd data
 python convert.py
 cd ..
 ```
 
 step4: 训练
 
 ```
 python retinanet/main.py
 ```

 step5: 预测
 ```
 python retinanet/predict.py
 ```
 
 ## 4. 效果
 
 线上 0.97+
 
 ## 5. 参考
 
 [pytorch-retinanet](https://github.com/yhenon/pytorch-retinanet)
 
 ## 6. 提醒
 
 如有疑问，请提出 issue，编码问题请自行谷歌。
