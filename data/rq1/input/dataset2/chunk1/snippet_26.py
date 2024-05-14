#Source: https://stackoverflow.com/questions/44307828/export-a-tex-file-file-from-python-script-typeerror-a-float-is-required
with open(directoryPath + os.sep +'commonTables3.tex','w') as f:
    f.write(content%({'index':str(3)}))