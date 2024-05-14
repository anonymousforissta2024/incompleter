#Source: https://stackoverflow.com/questions/42427389/typeerror-str-object-is-not-callable
class Parser(object):

    def __init__(self, inputFile): # initalizer / constructor
        #open input file and gets ready to parse it
        f = open(inputFile, "r")
        self.commands = list(f)
        f.close()
        print(self.commands)
        self.currentCommand = 0
        self.index = 0

    def hasMoreCommands(self):
        #are there any more commands in the input
        #returns boolean
        if (self.commands[self.currentCommand][self.index] == "\\")  and (self.commands[self.currentCommand][self.index+1] == "n"): # checks for "/n", alluding that the command has ended and we can advance to the next command
            return True
        else:
            return False

    def advance(self):
        #reads next command and makes it current command
        #called only if hasMoreCommands is true
        if self.hasMoreCommands():
            self.currentCommand += 1

    def commandType(self):
        #returns type of current command A_COMMAND, C_COMMAND, L_COMMAND
        #C A or L(psuedo command for (XxX))
        #dest=comp; jmp, @, ()
        self.type = self.commands[self.currentCommand][0]
        if self.type == "@":
            return "A_COMMAND"
        elif self.type == "(":
            return "L_COMMAND"
        else:
            return "C_COMMAND"

    def dest(self):
        #returns dest mnemoic of current C instruction - 8 Poss
        #called when command type is C
        #return string
        if (self.commandType() == "C_COMMAND") and ("=" in self.commands[self.currentCommand]):
                return self.commands[self.currentCommand][0:(self.commands[self.currentCommand].index("="))]

def main(inputFile):
    d = Parser(inputFile)
    d.commandType = "C_COMMAND"
    d.commands = ["D=A+2\\n", "AMD=A+5\\n"]
    d.currentCommand = 0
    print(d.dest())

main("/Users/user1/Desktop/filelocation/projects/06/add/add.asm")