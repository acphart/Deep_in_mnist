# Deep_in_mnist
- 基于`mnist`手写数字数据集, 试验各种神经网络算法和优化技术；
- 这是关于`mnist`识别项目研究论文的一个汇总：[rodrigob.github.io : Classifiction datasets results](http://rodrigob.github.io/are_we_there_yet/build/classification_datasets_results.html#4d4e495354) 
- 关于正确率，这里将`70000`个完整数据分为训练集`（50000）`、验证集`（10000）`和测试集`（10000）`，使用训练集训练模型，并通过验证集选取最优模型，最后在测试集上测试最优模型，得到正确率。
## 文件说明
### 1. mnist.pkl.gz
- 这是一个包装很好的`mnist`数据集，包含所有原始的`mnist`数据；
- 里面的数据分为3部分，训练集、验证集和测试集，每个数据集都是`(X, y)`格式，`X`、`y`分别为特征数组和标签数组。
- 我在本地电脑上将其转换成了单个`csv`文件，不过文件大小超过了上传限制，所以这里又上传了我的格式转换代码`save_all_mnist_to_csv.py`。
- 另外需要提醒一下，这个数据集里面的特征数组已经归一化了。
### 2. save_all_mnist_to_csv.py
- 提取`mnist.pkl.gz`中的数据，得到一个完整数据的`.csv`文件，其中数据的大小为`（70000, 785）`，共`70000`个样例，其中标签在第一列。
### 训练文件
- 包含六个训练文件，均是 Jupyter notebook  文件，使用 `Keras` 框架。
- 可在下面点击相应的文件名，跳转到`nbviewer`直接查看对应内容，若需要在本地运行，请下载相应文件:)
- 从带一个隐藏层的多层感知机开始，到使用原版的`LeNet-5`架构，再通过优化`LeNet-5`（增加滤波器的数量，使用`Dropout`和`BatchNormal`），最后再进行图像增强，准确率从`0.9789`提升到`0.9954`。
- `img`文件夹里面是六个文件的可视化训练过程图
#### 1.[Keras_mnist_MLP-2L.9789.ipynb](https://nbviewer.jupyter.org/github/acphart/Deep_in_mnist/blob/master/Keras_mnist_MLP-2L.9789.ipynb)
#### 2.[Keras_mnist_LeNet-5_v1.9899.ipynb](https://nbviewer.jupyter.org/github/acphart/Deep_in_mnist/blob/master/Keras_mnist_LeNet-5_v1.9899.ipynb)
#### 3.[Keras_mnist_LeNet-5_v2.9929.ipynb](https://nbviewer.jupyter.org/github/acphart/Deep_in_mnist/blob/master/Keras_mnist_LeNet-5_v2.9929.ipynb)
#### 4.[Keras_mnist_LeNet-5_v2_DA_lr_BN.9947.ipynb](https://nbviewer.jupyter.org/github/acphart/Deep_in_mnist/blob/master/Keras_mnist_LeNet-5_v2_DA_lr_BN.9947.ipynb)
#### 5.[Keras_mnist_LeNet-5_v2_DA_lr.9952.ipynb](https://nbviewer.jupyter.org/github/acphart/Deep_in_mnist/blob/master/Keras_mnist_LeNet-5_v2_DA_lr.9952.ipynb)
#### 6.[Keras_mnist_LeNet-5_v2_DA_lr_BN_v2.9954.ipynb](https://nbviewer.jupyter.org/github/acphart/Deep_in_mnist/blob/master/Keras_mnist_LeNet-5_v2_DA_lr_BN_v2.9954.ipynb)
