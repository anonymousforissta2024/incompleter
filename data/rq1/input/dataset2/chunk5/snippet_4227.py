#Source: https://stackoverflow.com/questions/61899384/how-to-handle-python-subprocess-filenotfounderror-winerror-2
import ffmpeg_streaming
from ffmpeg_streaming import Formats, Bitrate, Representation, Size
import subprocess
import sys

def monitor(ffmpeg, duration, time_):
    per = round(time_ / duration * 100)
    sys.stdout.write("\rTranscoding...(%s%%) [%s%s]" % (per, '#' * per, '-' * (100 - per)))
    sys.stdout.flush()

video = ffmpeg_streaming.input('http://freja.hiof.no:1935/rtplive/_definst_/hessdalen03.stream/playlist.m3u8')

_360p = Representation(Size(640, 360), Bitrate(276 * 1024, 128 * 1024))
_480p = Representation(Size(854, 480), Bitrate(750 * 1024, 192 * 1024))
_720p = Representation(Size(1280, 720), Bitrate(2048 * 1024, 320 * 1024))

hls_stream = video.hls(Formats.h264(), hls_list_size = 1, hls_time = 60)
hls_stream.representations(_480p)
hls_stream.output('C:/Users/Documents/mashpy/VideoAnalytics_Mediaserver/ffmpeg_exec_test/video_fragments/hl_test.m3u8')