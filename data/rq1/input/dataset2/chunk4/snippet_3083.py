#Source: https://stackoverflow.com/questions/69499013/line-8-in-speak-voiceengine-getpropertyrate-100-typeerror-getproperty-t
import pyttsx3

# This function is used to process text and speak it out
def speak (lis):
    voiceEngine = pyttsx3.init() 
    voiceEngine.getProperty("rate", 100)
    #voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\IVONA 2 Voice Brian22" 
    #voiceEngine.setProperty('IVONA 2 Brian - British English male voice [22kHz]', voice_id ) 
    voiceEngine.say (lis)
    voiceEngine.runAndWait() 
    voiceEngine.stop


speak(lis = "Hello i am alpha, your personal digital assistant. how may i be of your assistance")