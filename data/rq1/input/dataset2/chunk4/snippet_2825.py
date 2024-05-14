#Source: https://stackoverflow.com/questions/56056538/attributeerror-io-textiowrapper-object-has-no-attribute-replace
artists = open('artists.txt') ## IF YOU WANT TO EDIT THE SONG NAMES AND ARTISTS
songs = open('songs.txt') ## YOU NEED TO LEAVE THEM IN ORDER

songfilter = 'abcdefghijklmnopqrstuvwxyz\/' #Lowercase Alphabet With Some Slashes To Remove "/n"

songsFiltered = [songs.replace(alphabet, '') for w in songs]

guessList = list(zip(artists, songs))

songSelect = random.choice(guessList)

print(songSelect)