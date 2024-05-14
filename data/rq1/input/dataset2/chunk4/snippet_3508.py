#Source: https://stackoverflow.com/questions/20051405/attribute-error-using-biopython-bio-searchio-convert
from Bio import SearchIO
import os

blast_out= "some_path"
parsed_out="some_path"

os.chdir(blast_out)
all_files = os.listdir(blast_out)

for single_file in all_files:
    print ("Current file is: " + single_file)

    #define handles
    in_file = single_file
    in_fmt = 'blast-xml'
    out_file = parsed_out + single_file + '.tab'
    out_fmt = 'blast-tab'
    out_kwarg = {'comments': True}

    SearchIO.convert(in_file, in_fmt, out_file, out_fmt, out_kwargs=out_kwarg)

print ("\nFinished Parsing File.\n")