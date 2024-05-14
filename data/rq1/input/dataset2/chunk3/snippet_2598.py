#Source: https://stackoverflow.com/questions/51644941/typeerror-csv-reader-object-is-not-subscriptable
#!/usr/bin/python
# -*- coding: utf-8 -*-
import csv

la = open('loginscruz.csv', 'r')
listaluno = csv.reader(la,delimiter=';')

for alunos in listaluno[1:]:

    num = 1

    aluno = str(alunos[3])

    if (aluno != ''):
        print (aluno + " batata")