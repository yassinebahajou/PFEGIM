import string
import librosa
import soundfile
import os, glob, pickle
import numpy as np
import pandas as pd
import xlsxwriter as xlsxwriter
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score, confusion_matrix

import seaborn as sns
import matplotlib.pyplot as plt


def extract_feature(file_name, mfcc, chroma, lpc,mel=True):
    with soundfile.SoundFile(file_name) as sound_file:
        X = sound_file.read(dtype="float32")
        sample_rate=sound_file.samplerate
        print("Extracting Features :"+file_name)
        if chroma:
            stft=np.abs(librosa.stft(X))
        result=np.array([])
        if mfcc:
            mfccs=np.mean(librosa.feature.mfcc(y=X, sr=sample_rate, n_mfcc=40).T, axis=0)
            # print(f'mfcc {mfccs}')
            # print(f'mfcc {len(mfccs)}')
            result=np.hstack((result, mfccs))

        if chroma:
            chroma=np.mean(librosa.feature.chroma_stft(S=stft, sr=sample_rate).T,axis=0)

            # print(f'charoma {chroma}')
            # print(f'charoma {len(chroma)}')
            result=np.hstack((result, chroma))
        if lpc:
            lpc=librosa.core.lpc(X, 12)
            # print(f'mel {len(mel)}')
            result=np.hstack((result, lpc))
        if mel:
            mel=np.mean(librosa.feature.melspectrogram(X, sr=sample_rate).T,axis=0)
            # print(f'mel {len(mel)}')
            result=np.hstack((result, mel))
        print("Extracting Features Done:" + file_name)
    return result


def export_features_advanced(features):
    current_file_features = 'extracted_features/test.xlsx'
    features_data = []
    worksheet_columns = list(string.ascii_uppercase)
    workbook = xlsxwriter.Workbook(current_file_features)
    worksheet = workbook.add_worksheet()
    features_names = ['mfcc', 'Chroma', 'melspectrogram']
    features_data.append(features[0:40])
    features_data.append(features[40:52])
    features_data.append(features[52:])

    for letter, feature_data in enumerate(features_data):
        print(letter)
        print(feature_data)
        worksheet.write(worksheet_columns[letter] + '1', features_names[letter])
        for i, data in enumerate(feature_data):
            print(i)
            print(data)
            worksheet.write(worksheet_columns[letter] + str(i + 2), data)

    workbook.close()


#DataFlair - Emotions in the RAVDESS dataset
emotions={
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
# observed_emotions=['neutral','calm','happy','sad','angry','fearful','disgust','surprised']

def load_data(test_size=0.33,file_path="D:\\DataFlair\\ravdess data"):
    x,y=[],[]
    for file in glob.glob(file_path+"\\Actor_*\\*.wav"):
        file_name=os.path.basename(file)
        print("Loading Audio File: ",file)
        emotion=emotions[file_name.split("-")[2]]
        if emotion in observed_emotions:
            try:
                feature=extract_feature(file, mfcc=True, chroma=True, lpc=True)
            except Exception:
                print("error reading audio file")
            else:
                x.append(feature)
                y.append(emotion)
        print("Loading Audio Done :" + file)
    return train_test_split(np.array(x), y, test_size=test_size, random_state=9)

#DataFlair - Initialize the Multi Layer Perceptron Classifier
def create_train_model(x_train,x_test,y_train,y_test):
    model = MLPClassifier(alpha=0.01, batch_size=256, epsilon=1e-08, hidden_layer_sizes=(300,), learning_rate='adaptive', max_iter=500)
    model.fit(x_train, y_train)

    return model

def detect_emotion(file_path, model):
    XX = []
    XX.append(extract_feature(file_path, mfcc=True, chroma=True, mel=True))
    return model.predict(XX)

def generate_confusion_matrics(model, x_test,y_test):
    y_pred = model.predict(x_test)
    accuracy = accuracy_score(y_true=y_test, y_pred=y_pred)
    cm = confusion_matrix(y_test, y_pred)
    print("cm", cm)
    # index = ['angry', 'calm', 'disgust', 'fearful', 'happy', 'neutral', 'sad', 'surprised']
    # columns = ['angry', 'calm', 'disgust', 'fearful', 'happy', 'neutral', 'sad', 'surprised']
    # index = ['angry', 'calm', 'fearful', 'happy', 'neutral', 'sad']
    # columns = ['angry', 'calm', 'fearful', 'happy', 'neutral', 'sad']
    # cm_df = pd.DataFrame(cm, index, columns)
    # plt.figure(figsize=(10, 6))
    # sns.heatmap(cm_df, annot=True)
    return accuracy, cm