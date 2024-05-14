#Source: https://stackoverflow.com/questions/64211907/incomprehensible-name-error-using-class-variables-within-a-class-in-python
import re
from better_profanity import profanity 


class Profanity(object):

    # Wordlist file paths for languages
    eng = "/home/mareike/sw_filter/wordlists/google_profanity_wordlist_eng.txt"
    deu = "/home/mareike/sw_filter/wordlists/profanity_wordlist_deu.txt"
    # Further language variables...

    

    def __init__(self, transcript_filename, wordlist_language):
        self.transcript_filename = transcript_filename
        self.wordlist_language = wordlist_language
        
        
    def load_transcript(self):
        f = open(self.transcript_filename, "r")
        file = f.read()
        f.close()

        return file
    

    def load_wordlist(self):
        f = open(self.wordlist_language, "r")
        file = f.read()
        f.close()

        return file


    def preprocess(self):
        # Remove noisy punctuation
        prep_transcript = transcript.replace('--', '').replace('>', '')
        prep_transcript = prep_transcript.replace('[', '').replace(']', '')
        prep_transcript = prep_transcript.replace('(', '').replace(')', '')
        prep_transcript = prep_transcript.replace("'", '')
        prep_transcript = prep_transcript.replace('.', '')
        prep_transcript = prep_transcript.replace(';', '')
        prep_transcript = prep_transcript.replace('!', '')
        prep_transcript = prep_transcript.replace('?', '')
        prep_transcript = prep_transcript.replace('-', ' ')
        prep_transcript = re.sub(r":\B", "", prep_transcript, flags = re.MULTILINE)
        prep_transcript = re.sub(r",\D\b", " ", prep_transcript, flags = re.MULTILINE)
        prep_transcript = re.sub(r",\n", "\n", prep_transcript, flags = re.MULTILINE)

        # Lowercase text
        prep_transcript = prep_transcript.lower()

        return prep_transcript


    def apply_filter(self, prep_transcript):
        if __name__ == "__main__":
            profanity.load_censor_words_from_file(self.wordlist_language)                                                                                                             
            censored_transcript = profanity.censor(prep_transcript)

        return censored_transcript


p = Profanity("sample_transcript.txt", eng)

transcript = p.load_transcript()
wordlist = p.load_wordlist()
prep_transcript = p.preprocess()

censored_transcript = p.apply_filter(prep_transcript)
print(censored_transcript)