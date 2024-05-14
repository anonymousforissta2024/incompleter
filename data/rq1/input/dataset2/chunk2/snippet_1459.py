#Source: https://stackoverflow.com/questions/63091432/typeerror-float-argument-must-be-a-string-or-a-number-not-polycollection
import librosa.display
ax1 = plt.subplot(gs[1])
y, sr = librosa.load("Audiofilepath")
ax1.plot(librosa.display.waveplot(y, sr))