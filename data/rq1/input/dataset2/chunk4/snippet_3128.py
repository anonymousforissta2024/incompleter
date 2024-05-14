#Source: https://stackoverflow.com/questions/71988882/attribute-error-property-object-has-no-attribute-object
from pytube import YouTube
import pytube

SAVE_PATH = "c:users\pavit\Desktop" #to_do


link=input("enter the link")

try:
    # object creation using YouTube
    # which was imported in the beginning
    yt = YouTube(link)
except:
    print("Connection Error") #to handle exception

mp4files = YouTube.streams.filter()
yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution')[-1].download()

d_video = yt.get(mp4files[-1].extension,mp4files[-1].resolution)
try:

    d_video.download(SAVE_PATH)
except:
    print("Some Error!")
print('Task Completed!')