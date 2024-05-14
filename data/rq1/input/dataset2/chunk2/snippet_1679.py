#Source: https://stackoverflow.com/questions/61823343/typeerror-python-ask-to-insert-self-argument
class debugger():
    def __init__(self, state=False):
        self.state = state

    def status(self, inp:bool):
        if inp == True and self.state == False: print('Debugger activated')
        elif inp == True and self.state == True: print('Debugger alredy started')
        elif inp == False and self.state == True: print('Debugger stopped')
        else: print('Debugger alredy stopped')
        self.state = inp

    def log(self, msg:str):
        if self.state == True: print(f'[DEBUGGER]: {msg}')
        else: pass

    def __repr__(self):
        if self.state == True: return 'Debugger status: Active'
        else: return 'Debugger status: Disabled'

debugger.status(True)
debugger()
debugger.log('Test from debugger')