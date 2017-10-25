# MachineLearning
去年一年Github上最热门的项目当属Google的TensorFlow无疑。
在之前做验证码识别的阶段，已经使用了SVM向量机的方法实现了数字验证码的识别。
开本工程的想法在于：使用验证码处理这一切入口，来进行Machine Learning的学习。

##一、Keras库
Keras库依赖backend, 使用TensorFlow或者Theano

>Centos6.4安装TensorFlow后,运行时会有如下报错:
```
/lib64/libc.so.6: version `GLIBC_2.14' not found
```
>建议直接使用Centos7

###1. CNN神经卷积网络

图片打码分类：
![index]()

模型:
![index]()

训练输出：
```
(pyenv3.6)$ python3 mykeras.py 
Using TensorFlow backend.
0123456789
channels_last
Train on 1184 samples, validate on 20 samples
Epoch 1/12
2017-10-25 10:03:36.913650: W tensorflow/core/platform/cpu_feature_guard.cc:45] The TensorFlow library wasn't compiled to use SSE4.1 instructions, but these are available on your machine and could speed up CPU computations.
2017-10-25 10:03:36.917306: W tensorflow/core/platform/cpu_feature_guard.cc:45] The TensorFlow library wasn't compiled to use SSE4.2 instructions, but these are available on your machine and could speed up CPU computations.
2017-10-25 10:03:36.917378: W tensorflow/core/platform/cpu_feature_guard.cc:45] The TensorFlow library wasn't compiled to use AVX instructions, but these are available on your machine and could speed up CPU computations.
2017-10-25 10:03:36.917432: W tensorflow/core/platform/cpu_feature_guard.cc:45] The TensorFlow library wasn't compiled to use AVX2 instructions, but these are available on your machine and could speed up CPU computations.
2017-10-25 10:03:36.917472: W tensorflow/core/platform/cpu_feature_guard.cc:45] The TensorFlow library wasn't compiled to use FMA instructions, but these are available on your machine and could speed up CPU computations.
1184/1184 [==============================] - 1s - loss: 11.7812 - acc: 0.2255 - val_loss: 1.4804 - val_acc: 0.8500
Epoch 2/12
1184/1184 [==============================] - 1s - loss: 8.7443 - acc: 0.4062 - val_loss: 1.1921e-07 - val_acc: 1.0000
Epoch 3/12
1184/1184 [==============================] - 1s - loss: 5.6381 - acc: 0.5988 - val_loss: 1.1921e-07 - val_acc: 1.0000
Epoch 4/12
1184/1184 [==============================] - 1s - loss: 3.7226 - acc: 0.7297 - val_loss: 1.1921e-07 - val_acc: 1.0000
Epoch 5/12
1184/1184 [==============================] - 1s - loss: 2.6180 - acc: 0.7973 - val_loss: 1.1921e-07 - val_acc: 1.0000
Epoch 6/12
1184/1184 [==============================] - 1s - loss: 2.2099 - acc: 0.8150 - val_loss: 1.1921e-07 - val_acc: 1.0000
Epoch 7/12
1184/1184 [==============================] - 1s - loss: 0.9495 - acc: 0.9096 - val_loss: 1.1921e-07 - val_acc: 1.0000
Epoch 8/12
1184/1184 [==============================] - 1s - loss: 0.7361 - acc: 0.9164 - val_loss: 1.1921e-07 - val_acc: 1.0000
Epoch 9/12
1184/1184 [==============================] - 1s - loss: 0.4811 - acc: 0.9409 - val_loss: 1.1921e-07 - val_acc: 1.0000
Epoch 10/12
1184/1184 [==============================] - 1s - loss: 0.3488 - acc: 0.9561 - val_loss: 1.1921e-07 - val_acc: 1.0000
Epoch 11/12
1184/1184 [==============================] - 1s - loss: 0.3312 - acc: 0.9578 - val_loss: 1.1921e-07 - val_acc: 1.0000
Epoch 12/12
1184/1184 [==============================] - 1s - loss: 0.2899 - acc: 0.9552 - val_loss: 1.1921e-07 - val_acc: 1.0000
Test loss: 1.19209289551e-07
Test accuracy: 1.0

```







##感谢
1. [使用 Keras 来破解 captcha 验证码](https://ypw.io/captcha/) https://ypw.io/captcha/
2. [卷积神经网络识别验证码模拟登录正方教务系统的尝试](http://www.jianshu.com/p/479dff9a599d) http://www.jianshu.com/p/479dff9a599d