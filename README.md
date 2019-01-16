## 1. 比赛地址

[智能盘点—钢筋数量AI识别](https://www.datafountain.cn/competitions/332/details)

## 2. 依赖

`pytorch0.4.1`,`opencv-python`,`skimage`

## 3. 使用方法

step0: 安装

```
git clone https://github.com/spytensor/detect_steel_bar
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
