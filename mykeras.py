import keras
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv2D, MaxPooling2D
from keras import backend
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

import os
WORK_PATH = r'~/tensorflow/crack'
os.chdir(WORK_PATH)
import string
CHRS = string.digits
print(CHRS)

num_classes = 10  # 共要识别的10个字符，(0-9),即10类
batch_size = 128
epochs =12

#输入图片的尺寸
img_rows, img_cols = 17, 12

#根据keras的后端是TensorFlow还是Theano转换输入形式
print(backend.image_data_format())
if backend.image_data_format() == 'channels_first':
    input_shape = (1, img_rows, img_cols)
else:
    input_shape = (img_rows, img_cols, 1)

import glob

X, Y = [], []
for dir in os.listdir(WORK_PATH):
    data_path = os.path.join(WORK_PATH, dir)
    if (os.path.isdir(data_path)):
        #遍历标记的文件夹下所有的图片
        for f in os.listdir(data_path):
            image_path = os.path.join(data_path, f)
            img = Image.open(image_path)
            t = 1.0 * np.array(img)
            t = t.reshape(*input_shape) # reshape后要赋值
            X.append(t) #验证码像素列表
            s = dir.split('_')[1]
            Y.append(CHRS.index(s)) #标签

X = np.stack(X)
Y = np.stack(Y)

# 对Y值进行one-hot编码 # 可尝试 keras.utils.to_categorical(np.array([0,1,1]), 3) 理解   
Y = keras.utils.to_categorical(Y, num_classes) 

split_point = len(Y) - 20  # 简单地分割训练集与测试集

x_train, y_train, x_test, y_test = X[:split_point], Y[:split_point], X[split_point:], Y[split_point:]

# 以下模型和mnist-cnn相同
# 两层3x3窗口的卷积(卷积核数为32和64)，一层最大池化(MaxPooling2D)
# 再Dropout(随机屏蔽部分神经元)并一维化(Flatten)到128个单元的全连接层(Dense)，最后Dropout输出到10个单元的全连接层（全部字符为10个）
model = Sequential()
model.add(Conv2D(32, kernel_size=(3, 3),
                 activation='relu',
                 input_shape=input_shape))                                                     
model.add(Conv2D(64, (3, 3), activation='relu'))                                               
model.add(MaxPooling2D(pool_size=(2, 2)))                                                      
model.add(Dropout(0.25))                                                                       
model.add(Flatten())                                                                           
model.add(Dense(128, activation='relu'))                                                       
model.add(Dropout(0.5))
model.add(Dense(num_classes, activation='softmax'))                                            
                                                                                               
model.compile(loss=keras.losses.categorical_crossentropy,                                      
              optimizer=keras.optimizers.Adadelta(),                                           
              metrics=['accuracy'])

model.fit(x_train, y_train,                                                                    
          batch_size=batch_size,                                                               
          epochs=epochs,
          verbose=1,
          validation_data=(x_test, y_test))                                                    
score = model.evaluate(x_test, y_test, verbose=0)                                              
print('Test loss:', score[0])
print('Test accuracy:', score[1])
model.save(r'../captcha.h5')
#可视化模型
from keras.utils.vis_utils import plot_model
plot_model(model, to_file="../image/model_cnn.png", show_shapes=True)
#打开图片
img = Image.open(r'../image/model_cnn.png')
plt.imshow(img)
plt.show()


