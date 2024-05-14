#Source: https://stackoverflow.com/questions/49304400/python-a-type-error-caused-by-what
import maya.cmds as mc

attributes = ['.t', '.r', '.s']

controllers = mc.ls('ctrl_Lip*', tr=True)

for controller in controllers:
    mc.duplicate(controller, n=controller+'_proxy')

def corresponding_proxy(controller):
    return controller+'_proxy'

for controller in controllers:
    for attr in attributes:
        mc.connectAttr(controller+attr, corresponding_proxy(controller)+attr)