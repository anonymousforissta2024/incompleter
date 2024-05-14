#Source: https://stackoverflow.com/questions/66599498/how-to-fix-pytube-error-attributeerror-nonetype-object-has-no-attribute-do
from pytube import YouTube

def dowload_vid(l, d):
    link = l.get()
    dir = d.get()

    try:
        vid = YouTube(link)
    except:
        print("Connection Error or Video doesn't exist")

    vid_res = vid.streams.get_highest_resolution()

    try:
        vid.streams.filter(res=vid_res).first().download(dir)
    except IndexError as e:
        print(e)