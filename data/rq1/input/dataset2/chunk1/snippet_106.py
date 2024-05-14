#Source: https://stackoverflow.com/questions/36077266/how-do-i-raise-a-filenotfounderror-properly
#!/usr/bin/env python3

import os

if not os.path.isfile("nothing.txt"):
    raise FileNotFoundError