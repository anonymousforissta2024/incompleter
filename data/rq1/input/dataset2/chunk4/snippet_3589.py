#Source: https://stackoverflow.com/questions/71594098/cant-solve-filenotfounderror-winerror-3-the-system-cannot-find-the-path-spec
dir = ('C://Users//zstanley//OneDrive - Golden Gate National Parks Conservancy//BolinasWyeWetlands')
os.chdir(dir)
[os.rename(os.path.join(dir, f), os.path.join(dir, f).replace('_', '').replace(' ', '').lower()) 
    for f in os.listdir(dir)]