#Source: https://stackoverflow.com/questions/70445787/jupyternotebook-filenotfounderror-winerror-3-the-system-cannot-find-the-path
#SETUP PATHS
POS_PATH = os.path.join('data', 'positive')
NEG_PATH = os.path.join('data', 'negative')
ANC_PATH = os.path.join('data','anchor')


#MAKE DIRECTORIES
os.makedirs(POS_PATH)
os.makedirs(NEG_PATH)
os.makedirs(ANC_PATH)