# Deep_in_mnist
- 基于mnist手写数字数据集, 试验各种神经网络算法和优化技术；
- 这是关于mnist识别项目研究论文的一个汇总：[rodrigob.github.io : Classifiction datasets results](http://rodrigob.github.io/are_we_there_yet/build/classification_datasets_results.html#4d4e495354) 
- 关于正确率，这里将70000个完整数据分为训练集（50000）、验证集（10000）和测试集（10000），使用训练集训练模型，并通过验证集选取最优模型，最后在测试集上测试最优模型，得到正确率。
## 文件说明
### 1. mnist.pkl.gz
- 这是一个包装很好的mnist数据集，包含所有原始的mnist数据；
- 里面的数据分为3部分，训练集、验证集和测试集，每个数据集都是(X, y)格式，X、y分别为特征数组和标签数组。
- 由于习惯于使用csv格式的数据，以及想自己调整三个数据集的大小，所以我在本地电脑上将其转换成了单个csv文件，不过文件大小超过了上传限制，所以这里又上传了我的格式转换代码save_all_mnist_to_csv.py。
- 另外需要提醒一下，这个数据集里面的特征数组已经归一化了。
### 2. save_all_mnist_to_csv.py
- 提取mnist.pkl.gz中的数据，得到一个完整数据的.csv文件，其中数据的大小为（70000, 785），共70000个样例，其中标签在第一列。
### 训练文件
- 包含六个训练文件，均是Jupyter notebook文件，使用Keras框架。
- 从带一个隐藏层的多层感知机开始，到使用原版的LeNet-5架构，再通过优化LeNet-5（增加滤波器的数量，使用Dropout和BatchNormal），最后再进行图像增强，准确率从0.9789提升到0.9954。
- img文件夹里面是六个文件的可视化训练过程图
#### 1.Keras_mnist_MLP-2L.9789.ipynb
#### 2.Keras_mnist_LeNet-5_v1.9899.ipynb
#### 3.Keras_mnist_LeNet-5_v2.9929.ipynb
#### 4.Keras_mnist_LeNet-5_v2_DA_lr_BN.9947.ipynb
#### 5.Keras_mnist_LeNet-5_v2_DA_lr.9952.ipynb
#### 6.Keras_mnist_LeNet-5_v2_DA_lr_BN_v2.9954.ipynb
