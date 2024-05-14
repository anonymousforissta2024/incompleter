#Source: https://stackoverflow.com/questions/42866418/using-absolute-path-filenotfounderror
#!/usr/bin/env python3
from os import system

def text_to_speech(word):
  system('say %s' % word)

with open(input("Input File Path: ")) as fin:
  for line in fin:
      text_to_speech(line)