#Source: https://stackoverflow.com/questions/72627886/pyinstaller-bundle-causes-filenotfounderror-with-multiprocessing-spawn-method
if __name__ == "__main__":
    freeze_support()
    set_start_method('spawn')