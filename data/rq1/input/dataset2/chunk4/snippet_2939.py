#Source: https://stackoverflow.com/questions/75781036/can-anyone-help-me-with-speech-emotion-classifier-i-dont-know-what-to-do-about
#Extract features (mfcc, chroma, mel) from a sound file
def extract_feature(file_name, **kwargs):
    mfcc = kwargs.get("mfcc")
    chroma = kwargs.get("chroma")
    mel = kwargs.get("mel")
    with soundfile.SoundFile(file_name) as sound_file:
        X = sound_file.read(dtype="float32")
        sample_rate=sound_file.samplerate
        if chroma:
            stft=np.abs(librosa.stft(X))
            result=np.array([])
        if mfcc:
            mfccs=np.mean(librosa.feature.mfcc(y=X, sr=sample_rate, n_mfcc=40).T, axis=0)
            result=np.hstack((result, mfccs))
        if chroma:
            chroma=np.mean(librosa.feature.chroma_stft(S=stft, sr=sample_rate).T,axis=0)
            result=np.hstack((result, chroma))
        if mel:
            mel=np.mean(librosa.feature.melspectrogram(X, sr=sample_rate).T,axis=0)
            result=np.hstack((result, mel))
    return result
# Emotions in the RAVDESS dataset
emotions={
  '01':'neutral',
  '02':'calm',
  '03':'happiness',
  '04':'sadness',
  '05':'angry',
  '06':'fearful',
  '07':'disgust',
  '08':'surprised'
}

#Emotions to observe
observed_emotions=['happiness', 'neutral', 'sadness']

#Load the data and extract features for each sound file
def load_data(test_size=0.2): 
    a,b=[],[]
    for file in glob.glob("/content/drive/MyDrive/Depression detection/speech-emotion-recognition-ravdess-data/Actor_*/*.wav"):
        file_name=os.path.basename(file)
        emotion=emotions[file_name.split("-")[2]]
        if emotion not in observed_emotions:
            continue
        feature=extract_feature(file, mfcc=True, chroma=True, mel=True)
        a.append(feature)
        b.append(emotion)
    return train_test_split(np.array(a), b, test_size=test_size, random_state=9)
#Split the dataset
atrain, atest, btrain, btest = load_data(test_size=0.25)