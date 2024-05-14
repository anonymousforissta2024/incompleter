#Source: https://stackoverflow.com/questions/55937881/how-to-fix-typeerror-introduced-by-switching-from-python-2-7-10-to-python-3-7
import subprocess

def getLength(filename):
  result = subprocess.Popen(["ffprobe", filename],
    stdout = subprocess.PIPE, stderr = subprocess.STDOUT)
  return [x for x in result.stdout.readlines() if "Duration" in x]

print(getLength('bell.mp4'))