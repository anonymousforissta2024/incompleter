#Source: https://stackoverflow.com/questions/60601415/subprocess-startupinfo-filenotfounderror
filepath = "C:/Users/Linus/Desktop/Test/Audio/"     #Input audio file path


from pydub import AudioSegment
import os

def mp3_to_wav(audio_file_name):
    if audio_file_name.split('.')[1] == 'mp3':    
        sound = AudioSegment.from_mp3(audio_file_name)
        audio_file_name = audio_file_name.split('.')[0] + '.wav'
        sound.export(audio_file_name, format="wav")

if __name__ == "__main__":
    for audio_file_name in os.listdir(filepath): 
        file_name = filepath + audio_file_name
        file_name = os.path.realpath(file_name)
        mp3_to_wav(file_name)