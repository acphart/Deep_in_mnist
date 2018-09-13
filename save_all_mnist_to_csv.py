import pickle
import gzip
import numpy as np
import pandas as pd

'''提取三个数据集'''
def load_data():
    f = gzip.open('./mnist.pkl.gz', 'rb')
    training_data, validation_data, test_data = pickle.load(f, encoding='iso-8859-1')
    f.close()
    return (training_data, validation_data, test_data)

tr_d, va_d, te_d = load_data()

'''获取各个数据集的特征数组和标签'''
tr_x, tr_y = tr_d[0], tr_d[1]
va_x, va_y = va_d[0], va_d[1]
te_x, te_y = te_d[0], te_d[1]

'''重新组合各个数据集，标签在第一列'''
tr = np.hstack((tr_y.reshape(50000, 1), tr_x))
va = np.hstack((va_y.reshape(10000, 1), va_x))
te = np.hstack((te_y.reshape(10000, 1), te_x))

'''组合成完整数据，打印其shape=(70000, 785)'''
all_mnist_data = np.vstack((tr, va, te))
print(all_mnist_data.shape)

'''通过pandas存为.csv文件'''
df = pd.DataFrame(all_mnist_data)
df.to_csv('./all_mnist_data.csv', index=False)

'''读取验证，没有问题'''
data = pd.read_csv('./all_mnist_data.csv')
print(data.head())