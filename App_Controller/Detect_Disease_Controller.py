import pickle

from keras.models import model_from_json

from App_Model.Keras_Model import extract_feature as keras_extracter
from App_Model.Sklearn_Model import extract_feature as sklearn_extracter


class Detect_Disease_Controller():
    def __init__(self):
        pass

    # def import_model(self,model_path):
    #     print("import controller model:")
    #     print(model_path)
    #     with open(model_path, "rb") as file:
    #         fstr = file.read()
    #         self.model = pickle.loads(fstr)
    #     print(self.model)

    def import_model(self,model_path):
        json_file = open(model_path, 'r')
        loaded_model_json = json_file.read()
        json_file.close()
        print("import model json")
        self.model = model_from_json(loaded_model_json)
        self.model.load_weights("model.h5")
        accuarcy = 70
        date_ = 22
        # load weights into new model
        # loaded_model.load_weights("model.h5")
        print("Loaded model from disk")

    def detect_disease(self):
        pass

# def get_audio_features(self):
    #     # X, sample_rate = librosa.load(audio_path, res_type='kaiser_fast', duration=2.5, sr=sampling_rate * 2,
    #     #                               offset=0.5)
    #     sample_rate = np.array(self.rate)
    #
    #     y_harmonic, y_percussive = librosa.effects.hpss(self.data)
    #     pitches, magnitudes = librosa.core.pitch.piptrack(y=self.data, sr=sample_rate)
    #
    #     mfccs = np.mean(librosa.feature.mfcc(y=self.data, sr=sample_rate, n_mfcc=13), axis=1)
    #
    #     pitches = np.trim_zeros(np.mean(pitches, axis=1))[:20]
    #
    #     magnitudes = np.trim_zeros(np.mean(magnitudes, axis=1))[:20]
    #
    #     C = np.mean(librosa.feature.chroma_cqt(y=y_harmonic, sr=(self.rate/2)), axis=1)
    #
    #     return [mfccs, pitches, magnitudes, C]
    #
    # def get_features_dataframe(self):
    #     features = pd.DataFrame(columns=['mfcc', 'pitches', 'magnitudes', 'C'])
    #     features.loc[0] = self.get_audio_features()
    #     mfcc = features.mfcc.apply(pd.Series)
    #     pit = features.pitches.apply(pd.Series)
    #     mag = features.magnitudes.apply(pd.Series)
    #     C = features.C.apply(pd.Series)
    #     print(mfcc.to_csv('mfcc.csv',index=False))
    #     combined_features = pd.concat([mfcc, pit, mag, C], axis=1, ignore_index=False)
    #
    #     return combined_features
    #
    # def export_features_advanced(self):
    #     self.current_file_features = 'extracted_features/' + self.song_name.split('.')[0] + '.xlsx'
    #     worksheet_columns =list(string.ascii_uppercase)
    #     features_data = self.get_audio_features()
    #     # self.current_file_features = '../extracted_features/test002.xlsx'
    #     workbook = xlsxwriter.Workbook(self.current_file_features)
    #     worksheet = workbook.add_worksheet()
    #     # time = np.arange(0, self.duration, self.duration / len(features_data[0]))
    #     # worksheet.write(worksheet_columns[0]+'1', 'MFC_Time')
    #     # for i in range(0, len(self.features_data[0])):
    #     #     worksheet.write(worksheet_columns[0] + str(i + 2), time[i])
    #     features_names = ['mfcc', 'pitche', 'magnitude', 'Chroma']
    #     for letter,feature_data in enumerate(features_data):
    #         print(letter)
    #         print(feature_data)
    #         worksheet.write(worksheet_columns[letter] + '1', features_names[letter])
    #         for i, data in enumerate(feature_data):
    #             print(i)
    #             print(data)
    #             worksheet.write(worksheet_columns[letter] + str(i + 2), data)
    #
    #     workbook.close()



