#Source: https://stackoverflow.com/questions/31497208/python-3-why-am-i-getting-an-attributeerror
import sys
from Parser import AssemblyParser
from Code import Code

parser = AssemblyParser(sys.argv[1])
translator = Code()

out_file = str(sys.argv[1]).split(".")
out_file = str(out_file[:1]) + ".hack"

with open(out_file, 'w', encoding='utf-8') as f:
    while parser.hasMoreCommands():
        parser.advance()
        if parser.commandType() == "A_COMMAND":
            dec_num = parser.symbol()
            binary = "{0:b}".format(dec_num)
        elif parser.commandType() == "C_COMMAND":
            default_bits = "111"
            comp_bits += translator.comp(parser.comp())
            dest_bits += translator.dest(parser.dest())
            jump_bits += translator.jump(parser.jump())
            binary = default_bits + comp_bits + dest_bits + jump_bits
        assert len(binary) == 16
        f.write(binary)