import glob
import os
import librosa
import numpy as np
import soundfile
from keras.models import Sequential
from keras.layers import Dense, Activation
from keras.layers import Dropout
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


#DataFlair - Emotions in the RAVDESS dataset
emotions_dict={
  '01':'neutral',
  '02':'calm',
  '03':'happy',
  '04':'sad',
  '05':'angry',
  '06':'fearful',
  '07':'disgust',
  '08':'surprised'
}
#DataFlair - Emotions to observe
# observed_emotions=['calm', 'happy', 'fearful', 'disgust']
observed_emotions=['neutral', 'calm', 'happy', 'sad', 'angry', 'fearful']


def extract_feature(file_name):
    print("Extracting Features :"+file_name)
    with soundfile.SoundFile(file_name) as sound_file:
        X = sound_file.read(dtype="float32")
        sample_rate=sound_file.samplerate
        stft = np.abs(librosa.stft(X))
        mfccs = np.mean(librosa.feature.mfcc(y=X, sr=sample_rate, n_mfcc=40).T, axis=0)
        chroma = np.mean(librosa.feature.chroma_stft(S=stft, sr=sample_rate).T, axis=0)
        mel = np.mean(librosa.feature.melspectrogram(X, sr=sample_rate).T, axis=0)
        # print("mel",len(mel))
        # contrast = np.mean(librosa.feature.spectral_contrast(S=stft, sr=sample_rate).T, axis=0)
        # tonnetz = np.mean(librosa.feature.tonnetz(y=librosa.effects.harmonic(X),
        # sr=sample_rate).T, axis=0)
        lpc = librosa.core.lpc(X, 12)

    print("Extracting Features Done:" + file_name)
    return mfccs,chroma,mel,lpc

def parse_audio_files(parent_dir,sub_dirs,file_ext="*.wav"):
    features, labels = np.empty((0,193)), np.empty(0)
    for label, sub_dir in enumerate(sub_dirs):
        for fn in glob.glob(os.path.join(parent_dir, sub_dir, file_ext)):
            emotion = emotions_dict[fn.split('\\')[-1].split('-')[2]]
            if emotion in observed_emotions:
                print("Loading Audio :" + fn)
                try:
                  # mfccs, chroma, mel, contrast,tonnetz = extract_feature(fn)

                  mfccs, chroma, mel,lpc = extract_feature(fn)
                except Exception as e:
                  print ("Error encountered while parsing file: ", fn)
                  continue
                # ext_features = np.hstack([mfccs,chroma,mel,contrast,tonnetz])
                ext_features = np.hstack([mfccs,chroma,mel,lpc])
                # print("hereee",len(ext_features))
                features = np.vstack([features,ext_features])
                # print("halala ..."+str(fn))
                # print("halala ..."+str(fn.split('\\')[-1]))
                labels = np.append(labels, fn.split('\\')[-1].split('-')[2])
                print("emotion ",fn.split('\\')[-1].split('-')[2])
                print("Loading Audio Done:" + fn)
    return np.array(features), np.array(labels, dtype = np.int)

def one_hot_encode(labels):
    n_labels = len(labels)
    n_unique_labels = len(np.unique(labels))
    one_hot_encode = np.zeros((n_labels,n_unique_labels+1))
    one_hot_encode[np.arange(n_labels), labels] = 1
    one_hot_encode=np.delete(one_hot_encode, 0, axis=1)
    return one_hot_encode

def load_data(test_size=0.33,main_dir = 'D:\DataFlair\Audio_Song_Actors_01-24'):
    pass
    #change the main_dir acordingly....
    sub_dir=os.listdir(main_dir)

    print ("\ncollecting features and labels..."+str(sub_dir))
    print("\nthis will take some time...")
    features, labels = parse_audio_files(main_dir,sub_dir)
    print("done")
    # np.save('X',features)
    # #one hot encoding labels
    # labels = one_hot_encode(labels)
    # np.save=('y', labels)
    #
    # X=np.load('X.npy')
    # y=np.load('y.npy')

    X = features
    y = one_hot_encode(labels)

    train_x, test_x, train_y, test_y = train_test_split(X, y, test_size=test_size, random_state=42)
    return train_x, test_x, train_y, test_y

# print("x",train_x.shape)
# print("y",train_y.shape)
# #dnn parameters
# n_dim = train_x.shape[1]
# n_classes = train_y.shape[1]
# n_hidden_units_1 = n_dim
# n_hidden_units_2 = 400 # approx n_dim * 2
# n_hidden_units_3 = 200 # half of layer 2
# n_hidden_units_4 = 100

#defining the model
def create_model( n_hidden_units_1, n_hidden_units_2 , n_hidden_units_3 , n_hidden_units_4 ,n_dim,n_classes,
                  activation_function='relu', init_type='normal', optimiser='adam', dropout_rate=0.2):
    model = Sequential()
    # layer 1
    model.add(Dense(n_hidden_units_1, input_dim=n_dim, init=init_type, activation=activation_function))
    # layer 2
    model.add(Dense(n_hidden_units_2, init=init_type, activation=activation_function))
    model.add(Dropout(dropout_rate))
    # layer 3
    model.add(Dense(n_hidden_units_3, init=init_type, activation=activation_function))
    model.add(Dropout(dropout_rate))
    #layer4
    model.add(Dense(n_hidden_units_4, init=init_type, activation=activation_function))
    model.add(Dropout(dropout_rate))
    # output layer
    model.add(Dense(n_classes, init=init_type, activation='softmax'))
    #model compilation
    model.compile(loss='categorical_crossentropy', optimizer=optimiser, metrics=['accuracy'])
    return model

# #create the model
# model = create_model()
# print("model",model)
#train the model
def train_model(model,train_x, train_y):
    history = model.fit(train_x, train_y, epochs=200, batch_size=4)
    return model

emotions=['neutral', 'calm', 'happy', 'sad', 'angry', 'fearful', 'disgust', 'surprised']
def generate_confusion_matrics(model, test_x,test_y):
    #predicting from the model
    predict=model.predict(test_x,batch_size=4)

    #predicted emotions from the test set
    y_pred = np.argmax(predict, 1)
    print("y_test",test_y)
    print("y_pred",y_pred)
    predicted_emo=[]
    for i in range(0,test_y.shape[0]):
        print("pred",y_pred[i])
        print("pred emo",emotions[y_pred[i]])
        emo=emotions[y_pred[i]]
        predicted_emo.append(emo)

    actual_emo=[]
    y_true=np.argmax(test_y, 1)
    for i in range(0,test_y.shape[0]):
      emo=emotions[y_true[i]]
      actual_emo.append(emo)
    print("predict emo:",predicted_emo)
    print("actual emo:",actual_emo)
    accuracy = accuracy_score(y_true=actual_emo, y_pred=predicted_emo)
    print("auccuracy", accuracy)
    #generate the confusion matrix
    cm =confusion_matrix(actual_emo, predicted_emo)
    print("cm",cm)
    # index = ['angry', 'calm', 'disgust', 'fearful', 'happy', 'neutral', 'sad', 'surprised']
    # columns = ['angry', 'calm', 'disgust', 'fearful', 'happy', 'neutral', 'sad', 'surprised']
    # index = ['angry', 'calm', 'fearful', 'happy', 'neutral', 'sad']
    # columns = ['angry', 'calm', 'fearful', 'happy', 'neutral', 'sad']
    # cm_df = pd.DataFrame(cm,index,columns)
    # plt.figure(figsize=(10,6))
    # sns.heatmap(cm_df, annot=True)
    return accuracy,cm

def detect_emotion(file_path, model):
    features, labels = np.empty((0, 193)), np.empty(0)
    # mfccs, chroma, mel, contrast, tonnetz = extract_feature(file_path)
    mfccs, chroma,mel, lpc = extract_feature(file_path)
    # ext_features = np.hstack([mfccs, chroma, mel, contrast, tonnetz])
    ext_features = np.hstack([mfccs, chroma,mel, lpc])
    features = np.vstack([features, ext_features])
    pred = model.predict(np.array(features))
    y_pred = np.argmax(pred, 1)
    print("pred",y_pred)
    print("pred",y_pred[0])
    print("emo",emotions[y_pred[0]])
    return emotions[y_pred[0]]