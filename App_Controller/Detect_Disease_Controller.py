import pickle

from keras.models import model_from_json

from App_Model.Keras_Model import extract_feature as keras_extracter
from App_Model.Sklearn_Model import extract_feature as sklearn_extracter
import keras
import tensorflow as tf
from keras.layers import Dense, Conv2D, MaxPool2D, Dropout, Flatten
from keras.models import Sequential
from keras.preprocessing import image

class Detect_Disease_Controller():
    def __init__(self):
        self.classes = ["Normal","Infected"]

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

    # def import_model(self,model_path):
    #     print("import controller model:")
    #     print(model_path)
    #     with open(model_path, "rb") as file:
    #         fstr = file.read()
    #         self.model = pickle.loads(fstr)
    #     print(self.model)

    def import_model(self,model_path):
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
        path = "D:/workstation/Config/cp.ckpt"
        self.init_model()
        self.model.load_weights(path)
        print("Loaded model from disk")
        print(self.model)


    def detect_disease(self,img):
        emotion = self.model.predict(img)
        # print((emotion > 0.5).astype("int32"))
        # print((emotion > 0.5).astype("int32")[0][0])
        indice = (emotion > 0.5).astype("int32")[0][0]
        return self.classes[indice]




