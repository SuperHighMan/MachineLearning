#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : my_cnn_predict.py
# @Author: Hui
# @Date  : 2017/10/25
# @Desc  :

'''
本程序用于批量预测模型，查看学习出来的验证码是否准确

'''

from keras.models import load_model
from keras import backend
import numpy as np
import os
from PIL import Image
from my_cnn import img_rows,img_cols, CHRS

MODEL = os.environ['HOME'] + r'/tensorflow/captcha.h5'

#根据keras的后端是TensorFlow还是Theano转换输入形式

if backend.image_data_format() == 'channels_first':
    input_shape = (1, img_rows, img_cols)
else:  #TensorFlow
    input_shape = (img_rows, img_cols, 1)

#载入训练好的模型
model = load_model(MODEL)

def predict_image(img):
    '''
    :param img: Pillow.Image
    :return: the result of predict
    '''
    X = []
    t = 1.0 * np.array(img)
    t = t.reshape(*input_shape)
    X.append(t)
    X = np.stack(X)
    Y = model.predict(X)
    result = CHRS[Y[0].argmax()]
    return result

def test():
    parent_path = os.path.join(os.environ['HOME'], 'tensorflow/predict')
    os.chdir(parent_path)
    for f in os.listdir(parent_path):
        img = Image.open(f)
        value = predict_image(img)
        print('%s : %s' %(f, value))

if __name__=='__main__':
    print('Start predict...')
    test()
    print('Thanks for testing...')