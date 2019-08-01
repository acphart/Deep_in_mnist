# Deep_in_mnist
- 基于mnist手写数字数据集, 试验各种神经网络算法和优化技术；
- 这是关于mnist识别项目研究论文的一个汇总：[rodrigob.github.io : Classifiction datasets results](http://rodrigob.github.io/are_we_there_yet/build/classification_datasets_results.html#4d4e495354) 
- 关于正确率，每一个项目都是将总共70000个完整数据分为训练集（60000）和测试集（10000），训练集的数据会在设计和训练算法模型时被相应处理（包括再次划分为训练集和验证集），待模型训练完成后用测试集进行测试，得到正确率。
## 文件说明
### 1. mnist.pkl.gz
- 这是一个包装很好的mnist数据集，包含所有原始的mnist数据；
- 里面的数据分为3部分，训练集、验证集和测试集，每个数据集都是(X, y)格式，X、y分别为特征数组和标签数组。
- 由于习惯于使用csv格式的数据，以及想自己调整三个数据集的大小，所以我在本地电脑上将其转换成了单个csv文件，不过文件大小超过了上传限制，所以这里又上传了我的格式转换代码save_all_mnist_to_csv.py。
- 另外需要提醒一下，这个数据集里面的特征数组已经归一化了。
### 2. save_all_mnist_to_csv.py
- 提取mnist.pkl.gz中的数据，得到一个完整数据的.csv文件，其中数据的大小为（70000, 785），共70000个样例，其中标签在第一列。
### 5. CNN_by_TensorFlow_with_LeNet-5_Architecture.ipynb
- [使用TensorFlow搭建卷积神经网络（LeNet-5）识别mnist手写数字（正确率99.29%）](https://www.jianshu.com/p/c99259abefb2)
- 参考LeNet-5架构，论文阅读及下载地址：http://yann.lecun.com/exdb/publis/pdf/lecun-98.pdf
