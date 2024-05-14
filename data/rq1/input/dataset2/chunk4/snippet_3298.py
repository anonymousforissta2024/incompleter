#Source: https://stackoverflow.com/questions/73933775/attributeerror-enter-when-using-with-taglib-filepath
import os
import subprocess
import taglib
import sys

def set_song_metadata_by_path(path, inviter, duetpartner):
   #with taglib.File(path, save_on_exit=True) as song:
   with taglib.File(path) as song:
       song.tags["ALBUM"] = inviter
       song.tags["ARTIST"] = inviter + duetpartner
       song.save()

# wipe metadata
def wipe_metadata(filetowipemetadata, output):
   if subprocess.call('ffmpeg -y -i "%s" -map_metadata -1 -c:v copy -c:a copy "%s"' % (filetowipemetadata, output), shell=True):
        sys.stderr.write("Error remuxing '%s', skipping." % (filetowipemetadata))
# here was continue, but no loop hence this

wipe_metadata('bored.m4a', 'bored2.m4a')
set_song_metadata_by_path('./bored2.m4a', 'test1', 'test2')