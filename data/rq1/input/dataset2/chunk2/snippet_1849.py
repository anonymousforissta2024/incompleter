#Source: https://stackoverflow.com/questions/57443462/filenotfounderror-winerror-2-the-system-cannot-find-the-file-specified-exift
import exiftool

files = ['file.MP4', 'file.MP4']

with exiftool.ExifTool() as et:
    metadata = et.get_metadata_batch(files)
for d in metadata:
    print("{:20.20} {:20.20}".format(d["SourceFile"],
                                     d["EXIF:DateTimeOriginal"]))