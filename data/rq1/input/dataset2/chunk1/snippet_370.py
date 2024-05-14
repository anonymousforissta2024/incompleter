#Source: https://stackoverflow.com/questions/62453020/attributeerror-nonetype-object-has-no-attribute-media-player-new
import vlc

media = vlc.MediaPlayer('annonce.mp4')
media.play()