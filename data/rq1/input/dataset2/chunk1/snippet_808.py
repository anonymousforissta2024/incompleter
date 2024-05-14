#Source: https://stackoverflow.com/questions/29113675/python-3-getting-file-not-found-error-on-absolute-path
filepath    =   os.path.join(webDir,size,imdbid + '.' + filetype);
f           =   open(filepath, "wb");