from datetime import datetime
import pickle
import os
import numpy as np
import matplotlib.pyplot as plt
import cv2
import keras
import tensorflow as tf
from keras.preprocessing import image
import keras.backend as K
from keras.models import Model, Sequential
from keras.layers import Input, Dense, Flatten, Dropout, BatchNormalization
from keras.layers import Conv2D, SeparableConv2D, MaxPool2D, LeakyReLU, Activation
from keras.callbacks import ModelCheckpoint, ReduceLROnPlateau, EarlyStopping
from sklearn.metrics import accuracy_score, confusion_matrix

from App_Model import Sklearn_Model as skl_model
from App_Model import Keras_Model as ks_model


class Train_Model_Controller():
    def __init__(self):
        self.x_test = None
        self.x_train = None
        self.img_dims = 150
        self.epochs = 10
        self.batch_size = 32

    def process_data(self,img_dims, batch_size,input_path):
        # Data generation objects
        train_datagen = image.ImageDataGenerator(rescale=1. / 255, zoom_range=0.3, vertical_flip=True)
        test_val_datagen = image.ImageDataGenerator(rescale=1. / 255)

        # This is fed to the network in the specified batch sizes and image dimensions
        train_gen = train_datagen.flow_from_directory(
            directory=input_path + '/train',
            target_size=(img_dims, img_dims),
            batch_size=batch_size,
            class_mode='binary',
            shuffle=True)

        test_gen = test_val_datagen.flow_from_directory(
            directory=input_path + '/test',
            target_size=(img_dims, img_dims),
            batch_size=batch_size,
            class_mode='binary',
            shuffle=True)

        # I will be making predictions off of the test set in one batch size
        # This is useful to be able to get the confusion matrix
        test_data = []
        test_labels = []

        for cond in ['/NORMAL/', '/PNEUMONIA/']:
            for img in (os.listdir(input_path + '/test' + cond)):
                img = plt.imread(input_path + '/test' + cond + img)
                img = cv2.resize(img, (img_dims, img_dims))
                img = np.dstack([img, img, img])
                img = img.astype('float32') / 255
                if cond == '/NORMAL/':
                    label = 0
                elif cond == '/PNEUMONIA/':
                    label = 1
                test_data.append(img)
                test_labels.append(label)

        test_data = np.array(test_data)
        test_labels = np.array(test_labels)

        return train_gen, test_gen, test_data, test_labels

    def load_data(self,file_path):
        self.train_gen, self.test_gen, self.test_data, self.test_labels = self.process_data(self.img_dims,self.batch_size,file_path)

    def load_data_(self, file_path):
        self.load_train_data(file_path)
        self.load_test_data(file_path)

    def load_train_data(self,file_path):
        train_datages = image.ImageDataGenerator(
            rescale=1 / 255, horizontal_flip=True, zoom_range=0.2, shear_range=0.2
        )
        self.x_train = train_datages.flow_from_directory(directory=file_path+"/train",
                                                       target_size=(256, 256), batch_size=1, class_mode='binary')
        print("classes:",self.x_train.class_indices)

    def load_test_data(self,file_path):
        test_datages = image.ImageDataGenerator(
            rescale=1 / 255
        )
        self.x_test = test_datages.flow_from_directory(directory=file_path+"/test",
                                                     target_size=(256, 256), batch_size=1, class_mode='binary')


    def init_model_1(self):
        self.model = Sequential()
        self.model.add(Conv2D(filters=32, kernel_size=(3, 3), activation='relu', input_shape=(256, 256, 3)))

        self.model.add(Conv2D(filters=32, kernel_size=(3, 3), activation='relu'))
        self.model.add(MaxPool2D())
        self.model.add(Dropout(rate=0.25))

        self.model.add(Conv2D(filters=32, kernel_size=(3, 3), activation='relu'))
        self.model.add(MaxPool2D())
        self.model.add(Dropout(rate=0.25))

        self.model.add(Conv2D(filters=32, kernel_size=(3, 3), activation='relu'))
        self.model.add(MaxPool2D())
        self.model.add(Dropout(rate=0.25))

        self.model.add(Flatten())
        self.model.add(Dense(units=64, activation='relu'))
        self.model.add(Dropout(rate=0.50))
        self.model.add(Dense(units=1, activation='sigmoid'))

        self.model.compile(loss=keras.losses.binary_crossentropy, optimizer="adam", metrics=['acc'])


    def init_model(self,FileName):
        inputs = Input(shape=(self.img_dims, self.img_dims, 3))

        # First conv block
        x = Conv2D(filters=16, kernel_size=(3, 3), activation='relu', padding='same')(inputs)
        x = Conv2D(filters=16, kernel_size=(3, 3), activation='relu', padding='same')(x)
        x = MaxPool2D(pool_size=(2, 2))(x)

        # Second conv block
        x = SeparableConv2D(filters=32, kernel_size=(3, 3), activation='relu', padding='same')(x)
        x = SeparableConv2D(filters=32, kernel_size=(3, 3), activation='relu', padding='same')(x)
        x = BatchNormalization()(x)
        x = MaxPool2D(pool_size=(2, 2))(x)

        # Third conv block
        x = SeparableConv2D(filters=64, kernel_size=(3, 3), activation='relu', padding='same')(x)
        x = SeparableConv2D(filters=64, kernel_size=(3, 3), activation='relu', padding='same')(x)
        x = BatchNormalization()(x)
        x = MaxPool2D(pool_size=(2, 2))(x)

        # Fourth conv block
        x = SeparableConv2D(filters=128, kernel_size=(3, 3), activation='relu', padding='same')(x)
        x = SeparableConv2D(filters=128, kernel_size=(3, 3), activation='relu', padding='same')(x)
        x = BatchNormalization()(x)
        x = MaxPool2D(pool_size=(2, 2))(x)
        x = Dropout(rate=0.2)(x)

        # Fifth conv block
        x = SeparableConv2D(filters=256, kernel_size=(3, 3), activation='relu', padding='same')(x)
        x = SeparableConv2D(filters=256, kernel_size=(3, 3), activation='relu', padding='same')(x)
        x = BatchNormalization()(x)
        x = MaxPool2D(pool_size=(2, 2))(x)
        x = Dropout(rate=0.2)(x)

        # FC layer
        x = Flatten()(x)
        x = Dense(units=512, activation='relu')(x)
        x = Dropout(rate=0.7)(x)
        x = Dense(units=128, activation='relu')(x)
        x = Dropout(rate=0.5)(x)
        x = Dense(units=64, activation='relu')(x)
        x = Dropout(rate=0.3)(x)

        # Output layer
        output = Dense(units=1, activation='sigmoid')(x)

        # Creating model and compiling
        self.model = Model(inputs=inputs, outputs=output)
        self.model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

        # Callbacks
        self.checkpoint = ModelCheckpoint(filepath='model_weights/'+FileName+'/best_weights.hdf5', save_best_only=True, save_weights_only=True)
        self.lr_reduce = ReduceLROnPlateau(monitor='val_loss', factor=0.3, patience=2, verbose=2, mode='max')
        self.early_stop = EarlyStopping(monitor='val_loss', min_delta=0.1, patience=1, mode='min')



    def train_model_(self):
        print("train model")
        print("classes:", self.x_train.class_indices)
        print(self.x_train is None)
        print(self.x_test is None)
        path = "config/cp.ckpt"
        cp_callback = tf.keras.callbacks.ModelCheckpoint(path, save_weights_only = True, verbose = 1)

        self.model.fit(self.x_train, steps_per_epoch=8,
            epochs=10, validation_steps=2,
            validation_data=self.x_test, callbacks=[cp_callback])

    def train_model(self):
        self.hist = self.model.fit_generator(
            self.train_gen, steps_per_epoch=self.train_gen.samples // self.batch_size,
            epochs=self.epochs, validation_data=self.test_gen,
            validation_steps=self.test_gen.samples // self.batch_size, callbacks=[self.checkpoint, self.lr_reduce])
        preds = self.model.predict(self.test_data)
        self.acc = accuracy_score(self.test_labels, np.round(preds)) * 100
        self.cm = confusion_matrix(self.test_labels, np.round(preds))

    def load_image(self,file_path):
        self.img = image.load_img(file_path, target_size=(256, 256))
        self.img = image.img_to_array(self.img) / 255
        self.img = np.array([self.img])
        return self.img.shape

    def get_prediction(self):
        predictions = (self.model.predict(self.img) > 0.5).astype("int32")
        return predictions[0]

