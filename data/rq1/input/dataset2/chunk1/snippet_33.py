#Source: https://stackoverflow.com/questions/63796878/typeerror-unknown-type-gstfraction
import gi

gi.require_version('Gst', '1.0')
from gi.repository import Gst

Gst.init(None)

caps = Gst.Caps.from_string('video/x-h264,width=640,height=480,framerate={30/1, 20/1, 15/1, 1/1}')
structure = caps.get_structure(0)

width = structure.get_int('width').value
height = structure.get_int('height').value
framerates = structure.get_list('framerate').array

print('width = ', width)
print('height = ', height)
for i in range(framerates.n_values):
    print(' - framerate = ', framerates.get_nth(i))