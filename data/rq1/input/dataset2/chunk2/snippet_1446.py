#Source: https://stackoverflow.com/questions/68000190/why-i-get-attributeerror-class-class-name-has-no-attribute-attribute-name
class Parser:
    def __init__(self, inst, type):
        self.inst = inst.strip()
        self.type = None
        self.checkType()

    def checkType(self):
        if self.inst.startswith('//') or self.inst in ['\n', '\r\n']:
            return

        elif self.inst.startswith('@'):
            self.type = 'A'

        else:
            self.type = 'C'

def main():
    with open(sys.argv[1], 'r') as asm:
        for inst in asm:
                P = Parser.inst
                print(p.type)


if __name__ == "__main__":
    main()