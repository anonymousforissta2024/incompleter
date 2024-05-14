#Source: https://stackoverflow.com/questions/51232871/typeerror-a-bytes-like-object-is-required-not-str-espeakng
esng = ESpeakNG(voice='english-us')
esng.pitch = 32
esng.speed = 150
esng.say('Hello World!', sync=True)