#Source: https://stackoverflow.com/questions/53426857/typeerror-typedict-object-is-not-callable
class CData(BigEndianStructure):

  _fields_ = [("x", c_uint),
              ("y", c_uint*10)]

  _pack_ = 1  