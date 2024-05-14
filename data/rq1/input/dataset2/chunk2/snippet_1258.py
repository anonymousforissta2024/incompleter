#Source: https://stackoverflow.com/questions/54375286/typeerror-cannot-unpack-non-iterable-axessubplot-object
import pywt
import scipy.io.wavfile as wavfile

import matplotlib.pyplot as plt

rate,signal = wavfile.read('a0025.wav')
time = [x /rate for x in range(0,len(signal))]
tree = pywt.wavedec(data=signal[:1000], wavelet='db2', level=4, mode='symmetric')
print(len(tree))
newTree = [tree[0]*0, tree[1]*0, tree[2]*0, tree[3]*0, tree[4]]
recSignal = pywt.waverec(newTree,'db2')
fig, ax = plt.subplot(2, 1)
ax[0].plot(time[:1000], signal[:1000])
ax[0].set_xlabel('Czas [s]')
ax[0].set_ylabel('Amplituda')
ax[1].plot(time[:1000], recSignal[:1000])
ax[1].set_xlabel('Czas [s]')
ax[1].set_ylabel('Amplituda')
plt.show()