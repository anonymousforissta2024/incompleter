#Source: https://stackoverflow.com/questions/50763584/code-works-in-python-2-but-not-python3-typeerror-a-bytes-like-object-is-require
import os
import pickle

modelpath = "models/"

gmm_files = [os.path.join(modelpath,fname) for fname in 
          os.listdir(modelpath) if fname.endswith('.gmm')]

models    = [pickle.load(open(fname,'r')) for fname in gmm_files]