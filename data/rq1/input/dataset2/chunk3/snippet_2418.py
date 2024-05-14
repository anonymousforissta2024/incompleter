#Source: https://stackoverflow.com/questions/51028390/bottlepy-returning-typeerror-unhashable-type-set-with-if-clause
# -*- coding: utf-8 -*-

from bottle import route, template, request, post, run

@route('/')
def test_1():

    return template('test.html',
                    selected="F")

@post('/')
def response():
    pass

run(host='localhost', port=8409)