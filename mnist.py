import keras
from keras.layers import Convolution2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dense
from keras.models import Sequential
from keras.preprocessing.image import ImageDataGenerator
model = Sequential()
#convolution layer 1
model.add(Convolution2D(filters=32, kernel_size=(3,3), activation='relu',input_shape=(64, 64, 3)))
#pooling 
model.add(MaxPooling2D(pool_size=(2, 2))) 
#Flattening layer
model.add(Flatten())
#hidden layer
model.add(Dense(units=128, activation='relu'))
#output
model.add(Dense(units=6, activation='softmax'))
model.summary()
opt = keras.optimizers.Adam(learning_rate=0.0001)
model.compile(optimizer=opt, loss='binary_crossentropy', metrics=['accuracy'])
train_datagen = ImageDataGenerator( rescale=1./255, shear_range=0.2, zoom_range=0.2, horizontal_flip=True)
test_datagen = ImageDataGenerator(rescale=1./255)
training_set = train_datagen.flow_from_directory( '/dataset/seg_train', target_size=(64, 64), batch_size=32, class_mode='categorical')
test_set = test_datagen.flow_from_directory('/dataset/seg_test',target_size=(64, 64),batch_size=32,class_mode='categorical')
from keras.callbacks import ModelCheckpoint, EarlyStopping
checkpoint = ModelCheckpoint("intel.h5", monitor="val_loss", mode="min", verbose=1)
earlystop = EarlyStopping(monitor = 'val_loss', min_delta = 0, patience = 10, verbose = 1,restore_best_weights = True)
callbacks = [earlystop, checkpoint]
nb_train_samples = 14034
nb_validation_samples = 3000
epochs = 1
batch_size = 8
history = model.fit(training_set,steps_per_epoch = nb_train_samples // batch_size, epochs = epochs,callbacks = callbacks,validation_data=test_set, validation_steps = nb_validation_samples // batch_size)	
acc = history.history['accuracy']
l = len(acc)
final_acc = acc[l-1]
print(final_acc)
final_acc1 = 100 * final_acc
print(final_acc1)
str_final_acc = str(final_acc1)
f = open("/accuracy.txt", "w")
f.write(str_final_acc)
f.close()
