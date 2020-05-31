import os
import tensorflow as tf
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
import numpy as np 
import keras 
from keras.datasets import mnist 
from keras.models import Model 
from keras.models import Sequential
from keras.layers import Dense, Input
from keras.layers import Conv2D, MaxPooling2D, Dropout
from keras.layers import Flatten 
from keras import backend as k
#loading the data
(x_train, y_train), (x_test, y_test) = mnist.load_data(path='/task3/dataset/mnist.npz')
#shape
img_rows, img_cols=28, 28
#setting the input shape
if k.image_data_format() == 'channels_first': 
  x_train = x_train.reshape(x_train.shape[0], 1, img_rows, img_cols) 
  x_test = x_test.reshape(x_test.shape[0], 1, img_rows, img_cols) 
  inpx = (1, img_rows, img_cols) 
else: 
  x_train = x_train.reshape(x_train.shape[0], img_rows, img_cols, 1) 
  x_test = x_test.reshape(x_test.shape[0], img_rows, img_cols, 1) 
  inpx = (img_rows, img_cols, 1) 
#scaling the data
x_train = x_train.astype('float32') 
x_test = x_test.astype('float32') 
x_train /= 255
x_test /= 255
#one-hot-encoding
y_train = keras.utils.to_categorical(y_train) 
y_test = keras.utils.to_categorical(y_test)
#creating a model
model = Sequential()
#convolutional layer1
model.add(Conv2D(16, kernel_size=(3, 3), activation='relu', input_shape=inpx))
#pooling layer 
model.add(MaxPooling2D(pool_size=(2, 2)))
#flattening layer
model.add(Flatten())
#hidden layer 
model.add(Dense(8, activation='sigmoid'))
#output layer
model.add(Dense(10, activation='softmax'))
#summarizing
model.summary()
#compiling
model.compile(optimizer=keras.optimizers.Adadelta(), 
			loss=keras.losses.categorical_crossentropy, 
			metrics=['accuracy'])
#callbacks
from keras.callbacks import ModelCheckpoint, EarlyStopping
checkpoint = ModelCheckpoint("mnist.h5", monitor="val_loss", mode="min", verbose=1)
earlystop = EarlyStopping(monitor = 'val_loss', min_delta = 0, patience = 10, verbose = 1,restore_best_weights = True)
callbacks = [earlystop, checkpoint]
#training model
epochs = 1
model.fit(x_train, y_train, epochs = epochs, batch_size=8)
#testing model
score = model.evaluate(x_test, y_test, verbose=0) 
#print('loss=', score[0]) 
#print('accuracy=', score[1])
#getting model accuracy
acc=score[1]
final_acc=acc*100
print(final_acc)
str_final_acc=str(final_acc)
#saving model accuracy
f = open("/task3/accuracy.txt", "w")
f.write(str_final_acc)
f.close()
