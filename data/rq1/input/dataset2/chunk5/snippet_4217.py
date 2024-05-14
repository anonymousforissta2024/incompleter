#Source: https://stackoverflow.com/questions/59518408/mutagen-typeerror-a-bytes-like-object-is-required-not-str
audio = FLAC("music.flac")
audio['artist'] = sarki.artist.name
audio['title'] = sarki.name
pic = Picture()
pic.type = id3.PictureType.COVER_FRONT
pic.width = 640
pic.height = 640
pic.mime = 'image/jpeg'
pic.data = "music.jpg"

audio.add_picture(pic)
audio.save()