#Source: https://stackoverflow.com/questions/18872502/tarfile-addfile-gives-error-typeerror-str-does-not-support-the-buffer-interf
from io import StringIO
import tarfile

archive_files = []

data = ["DATA1 "]
data.append("DATA2 ")
archive_files.append(("FILE.txt", "\n".join(data)))

tar = tarfile.open ("file.tar", "w:tar")
for name, data in archive_files:
    info = tarfile.TarInfo(name)
    info.size = len(data)
    tar.addfile(info, StringIO(data))
tar.close()