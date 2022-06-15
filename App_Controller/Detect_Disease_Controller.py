import keras
import scipy
from keras.models import Model, Sequential
from keras.layers import Input, Dense, Flatten, Dropout, BatchNormalization
from keras.layers import Conv2D, SeparableConv2D, MaxPool2D
from keras import backend as K
# from keract import display_activations
import numpy as np

class Detect_Disease_Controller():
    def __init__(self):
        self.classes = ["Normale","Infecté"]
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

    def import_model(self,folder_name):
        path = "./model_weights/"+folder_name+"/best_weights.hdf5"
        self.init_model()
        self.model.load_weights(path)
        print("Loaded model from disk")
        print(self.model)
        print(self.model.summary())


    def detect_disease(self,img):
        emotion = self.model.predict(img)
        indice = (emotion > 0.5).astype("int32")[0][0]
        return self.classes[indice]

    def get_class_activation_map(self, img):
        '''
        this function computes the class activation map

        Inputs:
            1) model (tensorflow model) : trained model
            2) img (numpy array of shape (224, 224, 3)) : input image
        '''

        # expand dimension to fit the image to a network accepted input size
        img = np.expand_dims(img, axis=0)

        # predict to get the winning class
        predictions = self.model.predict(img)
        label_index = np.argmax(predictions)

        # Get the 2048 input weights to the softmax of the winning class.
        class_weights = self.model.layers[-1].get_weights()[0]
        class_weights_winner = class_weights[:, label_index]

        # get the final conv layer
        final_conv_layer = self.model.get_layer("dense_3")

        # create a function to fetch the final conv layer output maps (should be shape (1, 7, 7, 2048))
        get_output = K.function([self.model.layers[0].input], [final_conv_layer.output,self.model.layers[-1].output])
        [conv_outputs, predictions] = get_output([img])

        # squeeze conv map to shape image to size (7, 7, 2048)
        conv_outputs = np.squeeze(conv_outputs)

        # bilinear upsampling to resize each filtered image to size of original image
        mat_for_mult = scipy.ndimage.zoom(conv_outputs, (32, 32, 1), order=1)  # dim: 224 x 224 x 2048

        # get class activation map for object class that is predicted to be in the image
        final_output = np.dot(mat_for_mult.reshape((224 * 224, 2048)), class_weights_winner).reshape(224,224)  # dim: 224 x 224

        # return class activation map
        return final_output, label_index


