#Source: https://stackoverflow.com/questions/75461472/attributeerror-audio-object-has-no-attribute-to-intensity
data = Audio(file_path)
def _vad(sdata):
    intensity = data.to_intensity()
    intensity = intensity.values.squeeze()
    intensity[intensity <= 0] = 0
    intensity = _length(intensity)
    length= _length(intensity)
    intensity_mean = len(intensity)
    temp = []