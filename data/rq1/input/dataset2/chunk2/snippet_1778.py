#Source: https://stackoverflow.com/questions/27882285/blender-bge-import-nameerror
Controller = bge.logic.getCurrentController()
Owner = Controller.owner
Move = Controller.actuators['Spin']
PressLeft = Controller.sensors['SpinLeft']
PressRight = Controller.sensors['SpinRight']
Speed = Move.dRot[1]

if PressLeft.positive:
  Speed = Speed + 0.5
  Move.dRot = [0.0, Speed, 0.0]
  Controller.activate(Move)
elif PressRight.positive:
  Speed = Speed - 0.5
  Move.dRot = [0.0, Speed, 0.0]