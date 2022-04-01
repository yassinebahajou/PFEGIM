import librosa
import matplotlib.pyplot as plt
import scipy
import numpy as np
import soundfile

with soundfile.SoundFile("cutafew.wav") as sound_file:
    X = sound_file.read(dtype="float32")
    sample_rate = sound_file.samplerate
    a = np.mean(librosa.core.lpc(X, 127).T,axis=0)
    print(a)
    print(len(a))
# y, sr = librosa.load("cutafew.wav")
# a = librosa.core.lpc(y,13)
# pitches, magnitudes = librosa.piptrack(y=y, sr=sr)
# # librosa.feature.
# print(a)
# print(len(y))
# print(len(a))
# print(pitches)
# print(len(pitches))
# y_hat = scipy.signal.lfilter([0] + -1*a[1:], [1], y)
# plt.figure()
# plt.plot(y)
# plt.plot(y_hat, linestyle='--')
# plt.legend(['y', 'y_hat'])
# plt.title('LP Model Forward Prediction')
# plt.show()
# import librosa
# from scipy import io
# import numpy as np
# from spafe.utils import vis
# from spafe.features.lpc import lpc, lpcc
# from spafe.features.rplp import plp
# from spafe.features.mfcc import mfcc

# init input vars
# num_ceps = 13
# lifter = 0
# normalize = True

# read wav
# fs, sig = io.wavfile.read("cutafew.wav")
# sig,fs = librosa.load("cutafew.wav")
#
# # compute lpcs
# lpcs = np.mean(lpc(sig=sig, fs=fs, num_ceps=num_ceps).T, axis=0)
# print(lpcs)
# print(len(lpcs))
# #
# # # compute lpccs
# # lpccs = np.mean(lpcc(sig=sig, fs=fs, num_ceps=num_ceps, lifter=lifter, normalize=normalize).T, axis=0)
# # print(lpccs)
# # print(len(lpccs))
# #
# # # compute plps
# # plps = np.mean(plp(sig, fs, num_ceps).T, axis=0)
# # print(plps)
# # print(len(plps))
# #
# # # compute plps
# # # init input vars
# # num_ceps = 13
# # low_freq = 0
# # high_freq = 2000
# # nfilts = 24
# # nfft = 512
# # dct_type = 2
# # use_energy = True
# # lifter = 5
# # normalize = True
# # plps = np.mean(mfcc(sig=sig,
# #              fs=fs,
# #              num_ceps=num_ceps,
# #              nfilts=nfilts,
# #              nfft=nfft,
# #              low_freq=low_freq,
# #              high_freq=high_freq,
# #              dct_type=dct_type,
# #              use_energy=use_energy,
# #              lifter=lifter,
# #              normalize=normalize).T, axis=0)
# # print(plps)
# # print(len(plps))
# # # visualize features
# # # vis.visualize_features(lpcs, 'LPC Index', 'Frame Index')
# #
# #
# # # visualize spectogram
# # # vis.spectogram(sig, fs)
# #
# # # visualize features
# # # vis.visualize_features(lpccs, 'LPCC Index', 'Frame Index')