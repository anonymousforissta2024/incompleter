#Source: https://stackoverflow.com/questions/76137318/attributeerror-no-librosa-attribute-match-events
import librosa
import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
import sounddevice as sd
from scipy.spatial.distance import euclidean
from fastdtw import fastdtw
import os

#IMPORTAM VARIABILELE DIN FISIERUL secventa.py#################################
from secventa import semnal_secventa
from secventa import sr
from secventa import mfcc_matrix_secventa

  
#IMPORTAM VARIABILELE DIN FISIERUL cheie1.py###################################
from cheie1 import semnal_key
from cheie1 import mfcc_matrix_key


audio_dir = 'C:/Users/Daniel/OneDrive - Technical University of Cluj-Napoca/Desktop/Proiect_PSV/fisier_secvente'
audio_dir_key = 'C:/Users/Daniel/OneDrive - Technical University of Cluj-Napoca/Desktop/Proiect_PSV/fisier_cuv_cheie'

audio_files = os.listdir(audio_dir)
audio_files_key = os.listdir(audio_dir_key)

def find_keyword_time(audio_file_path, keyword):
    semnal, sr = librosa.load(audio_file_path, sr=16000)
    keyword_samples = librosa.samples_to_frames(librosa.match_events(librosa.onset.onset_detect(semnal), librosa.onset.onset_detect(keyword)))
    start_time = librosa.frames_to_time(keyword_samples[0], sr=sr)
    end_time = librosa.frames_to_time(keyword_samples[-1], sr=sr)
    print(f'Cuvantul cheie "{keyword}" se afla de la  {start_time} secunde pana la {end_time} secunde in secventa originala')

for file in audio_files:
    semnal_secventa, sr = librosa.load(os.path.join(audio_dir, file), sr=16000)
    found_keywords = []
    for file_key in audio_files_key:
        semnal_key, sr = librosa.load(os.path.join(audio_dir_key, file_key), sr=16000)
        step = 100
        nr_frames = int((len(semnal_secventa)-len(semnal_key))/step)
        D = np.zeros(nr_frames-1)
        for k in range(0, nr_frames - 1):
          signal1 = semnal_secventa[int(k*step):int(k*step) + len(semnal_key)-1]
          mfcc1 = librosa.feature.mfcc(y=signal1, sr=sr)
          mfcc2 = librosa.feature.mfcc(y=semnal_key, sr=sr)
          val, path = fastdtw(mfcc1.T, mfcc2.T, dist=euclidean)
          D[k] = val

        dist_min=np.amin(D)
        if dist_min < 300:
         index = np.where(D == dist_min)[0][0]
         found_keywords.append(file_key)

    if len(found_keywords) > 0:
     print(f"In secventa audio {file} am gasit cuvantul cheie {' si '.join(found_keywords)}")

     for keyword in found_keywords:
       semnal_key, sr = librosa.load(os.path.join(audio_dir_key, keyword), sr=16000)
       # Creare figura cu 2 subplot-uri   
       fig, (ax1, ax2) = plt.subplots(2, 1)

       # Plotare waveform in primul subplot
       librosa.display.waveshow(semnal_key, sr=sr, ax=ax1)
       ax1.set(title=f'Waveform pentru {keyword}', xlabel='Time', ylabel='Amplitude')

       # Plotare spectrograma in al doilea subplot
       D = np.abs(librosa.stft(semnal_key))
       img = librosa.display.specshow(librosa.amplitude_to_db(D, ref=np.max), y_axis='log', x_axis='time', ax=ax2)
       ax2.set(title='Spectrogram')
       fig.colorbar(img, ax=ax2, format='%+2.0f dB')
       
       # Find start and end time of keyword
       find_keyword_time(os.path.join(audio_dir_key, keyword), 'keyword')
    
       plt.tight_layout()
       plt.show()  
    else:
     print(f"In secventa audio {file} nu am gasit niciun cuvant cheie")