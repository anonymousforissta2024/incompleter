#Source: https://stackoverflow.com/questions/64006585/attributeerror-module-tensorflow-io-has-no-attribute-experimental
img = tfio.experimental.image.decode_tiff(img, channels=1)