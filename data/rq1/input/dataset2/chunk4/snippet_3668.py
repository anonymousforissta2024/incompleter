#Source: https://stackoverflow.com/questions/49304400/python-a-type-error-caused-by-what
import maya.cmds as mc

attributes = ['.t', '.r', '.s']

controllers = mc.ls('ctrl_Lip*')

def corresponding_proxy(controller):
    corresponding_proxy = mc.ls(controller+'_proxy')
    return corresponding_proxy

for controller in controllers :
    for attr in attributes :
        mc.connectAttr(controller+attr, corresponding_proxy(controller)+attr)