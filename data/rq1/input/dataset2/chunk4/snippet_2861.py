#Source: https://stackoverflow.com/questions/65541371/file-not-found-error-but-showing-contents-of-file-in-error
with  open("songs.txt","r") as filesongs: 
            songs=filesongs.read().replace('\n', '')

random=random.randint(0,3)
ransong=open("songs.txt","r").readline(0,random)