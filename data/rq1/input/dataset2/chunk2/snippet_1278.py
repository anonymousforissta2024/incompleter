#Source: https://stackoverflow.com/questions/65226109/pytube-error-attributeerror-nonetype-object-has-no-attribute-download
from pytube import YouTube
import pytube
yt_title = YouTube('https://www.youtube.com/watch?v=ZjDZrReZ4EI').title
ytd = YouTube('https://www.youtube.com/watch?v=ZjDZrReZ4EI').streams.first().download()