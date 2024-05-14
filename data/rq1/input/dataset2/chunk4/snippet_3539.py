#Source: https://stackoverflow.com/questions/67348417/attribute-error-python-pncc-using-spafe-module-scipy-has-no-attribute-fftpa
import scipy
from spafe.utils import vis
from spafe.features.pncc import pncc
import scipy.io.wavfile as wav

# init input vars
num_ceps = 13
low_freq = 0
high_freq = 2000
nfilts = 24
nfft = 512
dct_type = 2,
use_energy = False,
lifter = 5
normalize = True

# read wav
(fs, sig) = wav.read("sample.wav")

# compute features
pnccs = pncc(sig=sig,
             fs=fs,
             num_ceps=num_ceps,
             nfilts=nfilts,
             nfft=nfft,
             low_freq=low_freq,
             high_freq=high_freq,
             dct_type=dct_type,
             use_energy=use_energy,
             lifter=lifter,
             normalize=normalize)

# visualize spectogram
vis.spectogram(sig, fs)
# visualize features
vis.visualize_features(pnccs, 'PNCC Index', 'Frame Index')