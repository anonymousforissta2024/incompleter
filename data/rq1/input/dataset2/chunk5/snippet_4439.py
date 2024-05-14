#Source: https://stackoverflow.com/questions/72486540/filenotfounderror-the-system-cannot-find-the-file-specified
import requests
import ffmpeg
import sys
import os

in_filename = "ddd.mp4"
out_filename = "THUMBNAIL.jpg"


def generate_thumbnail(in_filename, out_filename):
    probe = ffmpeg.probe(in_filename)
    time = float(probe["streams"][0]["duration"]) // 2
    width = probe["streams"][0]["width"]
    try:
        (
            ffmpeg.input(in_filename, ss=time)
                .filter("scale", width, -1)
                .output(out_filename, vframes=1)
                .overwrite_output()
                .run(capture_stdout=True, capture_stderr=True)
        )
    except ffmpeg.Error as e:
        print(e.stderr.decode(), file=sys.stderr)
        sys.exit(1)


generate_thumbnail(in_filename, out_filename)