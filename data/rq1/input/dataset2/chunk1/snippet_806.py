#Source: https://stackoverflow.com/questions/54262306/ffmpeg-python-wrapper-ffmpeg-run-getting-filenotfounderror
import ffmpeg

videoInput = ffmpeg.input('vid.mp4')

videoOutput = videoInput.output('test.avi')

videoOutput.run()