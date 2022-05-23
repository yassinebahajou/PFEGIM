import pickle

from keras.models import model_from_json

from App_Model.Keras_Model import extract_feature as keras_extracter
from App_Model.Sklearn_Model import extract_feature as sklearn_extracter
import keras
import tensorflow as tf
from keras.layers import Dense, Conv2D, MaxPool2D, Dropout, Flatten
from keras.models import Sequential
from keras.preprocessing import image
from keras.models import Model, Sequential
from keras.layers import Input, Dense, Flatten, Dropout, BatchNormalization
from keras.layers import Conv2D, SeparableConv2D, MaxPool2D, LeakyReLU, Activation
from keras.callbacks import ModelCheckpoint, ReduceLROnPlateau, EarlyStopping

class Detect_Disease_Controller():
    def __init__(self):
        self.classes = ["Normal","Infected"]
        self.img_dims = 150
        self.epochs = 10
        self.batch_size = 32

    def init_model_(self):
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

    def init_model(self):
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

    # def import_model(self,model_path):
    #     print("import controller model:")
    #     print(model_path)
    #     with open(model_path, "rb") as file:
    #         fstr = file.read()
    #         self.model = pickle.loads(fstr)
    #     print(self.model)

    def import_model(self,folder_name):
        # json_file = open(model_path, 'r')
        # loaded_model_json = json_file.read()
        # json_file.close()
        # print("import model json")
        # self.model = model_from_json(loaded_model_json)
        # self.model.load_weights("model.h5")
        # accuarcy = 70
        # date_ = 22
        # # load weights into new model
        # # loaded_model.load_weights("model.h5")
        # print("Loaded model from disk")
        # path = "D:/workstation/Config/cp.ckpt"
        path = "./model_weights/"+folder_name+"/best_weights.hdf5"
        self.init_model()
        self.model.load_weights(path)
        print("Loaded model from disk")
        print(self.model)
        print(self.model.summary())


    def detect_disease(self,img):
        emotion = self.model.predict(img)
        # print((emotion > 0.5).astype("int32"))
        # print((emotion > 0.5).astype("int32")[0][0])
        indice = (emotion > 0.5).astype("int32")[0][0]
        return self.classes[indice]




