#Source: https://stackoverflow.com/questions/57371575/attributeerror-word-application-documents-with-win32-com-in-a-flask-application
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import string
import win32com.client
import nltk
import os
from collections import Counter
from pywintypes import com_error
from flask import request, Flask, render_template, jsonify

word = win32com.client.Dispatch("Word.Application")
word.Visible = False

app = Flask(__name__)
@app.route('/')
def landingPage():
    return render_template('homepage.html')

@app.route('/tokenizeDoc', methods = ['GET'])
def tokenizer():
    if request.method == 'GET':
        pathToProc = request.values.get("doc")
        sent_tokenizer = nltk.data.load('tokenizers/punkt/italian.pickle')
        it_stop_words = nltk.corpus.stopwords.words('italian') + ['\n', '\t', '']
        trashes = it_stop_words + list(string.punctuation)
        tokensTOT = []
        try:
            myDoc = word.Documents.Open(pathToProc, False, False, True) #ERROR!!!
            sentences = sent_tokenizer.tokenize(word.ActiveDocument.Range().Text)
            myDoc.Close()
            del myDoc
            for sentence in sentences:
                tokensTOT = tokensTOT + [t.lower() for t in nltk.word_tokenize(sentence) 
                                         if t.lower() not in trashes]
        except com_error:
            print('IMPOSSIBILE DECIFRARE IL FILE')
        return ''