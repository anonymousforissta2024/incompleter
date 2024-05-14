#Source: https://stackoverflow.com/questions/37632704/nameerror-when-running-pyglet
from pyglet.gl import *
from pyglet.window import key
from pyglet.window import mouse


window=pyglet.window.Window(resizable=True)

@window.event
def on_draw():

    glutInitDisplayMode (GLUT_RGB | GLUT_DOUBLE)
    glutInitWindowSize (width, height)
    glutInitWindowPosition (100, 100)


    glClearColor( 1.0, 1.0, 1.0, 1.0)
    glClear (GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    myObject ()
    glutSwapBuffers() 