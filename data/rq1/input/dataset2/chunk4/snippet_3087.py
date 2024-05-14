#Source: https://stackoverflow.com/questions/77195698/python3-typeerror-string-argument-expected-got-bytes
import subprocess    
from io import StringIO

image1, buffer1 = captureTestImage(str(cameraSettings), str(testWidth), str(testHeight))

imageData.write(subprocess.check_output(command, shell=True))