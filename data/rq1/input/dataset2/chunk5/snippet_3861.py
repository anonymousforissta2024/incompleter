#Source: https://stackoverflow.com/questions/51712554/system-path-check-has-typeerror-argument-of-type-nonetype-is-not-iterable
#!/usr/bin/env python3
import sys
from dotenv import load_dotenv, find_dotenv
from os import environ

# Add python project root folder to python path
load_dotenv(find_dotenv(), override=True, verbose=False)
PYTHON_SCRIPTS_DIR = environ.get('PYTHON_SCRIPTS_DIR')
PROJECT_DIR = environ.get('PROJECT_DIR')
sys.path.insert(0, PYTHON_SCRIPTS_DIR)

from evaluation.word_probability import WordFrequencyCounter