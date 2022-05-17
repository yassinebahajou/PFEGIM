from datetime import datetime
import pickle

import numpy as np
import matplotlib.pyplot as plt

import keras
import tensorflow as tf
from keras.layers import Dense, Conv2D, MaxPool2D, Dropout, Flatten
from keras.models import Sequential
from keras.preprocessing import image

from App_Model import Sklearn_Model as skl_model
from App_Model import Keras_Model as ks_model


class Train_Model_Controller():
    def __init__(self):
        self.x_test = None
        self.x_train = None

    def load_data(self, file_path):
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


    def init_model(self):
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

    def train_model(self):
        print("train model")
        print("classes:", self.x_train.class_indices)
        print(self.x_train is None)
        print(self.x_test is None)
        path = "config/cp.ckpt"
        cp_callback = tf.keras.callbacks.ModelCheckpoint(path, save_weights_only = True, verbose = 1)

        self.model.fit(self.x_train, steps_per_epoch=8,
            epochs=10, validation_steps=2,
            validation_data=self.x_test, callbacks=[cp_callback])

    def save_model(self):
        pickled_model_string = pickle.dumps(self.model)
        model_json = self.model.to_json()
        d = datetime.now().strftime("%d-%m-%Y %H=%M=%S")
        au = "80"
        with open("D:/workstation/MyModel/MyModel" + d + "_" + au + "_.json", "w") as json_file:
            print("saving..")
            json_file.write(model_json)

        self.model.save_weights("model.h5")
        print("model saved.")
        # with open("D:/workstation/MyModel/MyModel_" + d + "_" + au + "_.txt", "wb") as file:
        #
        #     file.write(pickled_model_string)

    def load_image(self,file_path):
        self.img = image.load_img(file_path, target_size=(256, 256))
        self.img = image.img_to_array(self.img) / 255
        self.img = np.array([self.img])
        return self.img.shape

    def get_prediction(self):
        predictions = (self.model.predict(self.img) > 0.5).astype("int32")
        return predictions[0]

