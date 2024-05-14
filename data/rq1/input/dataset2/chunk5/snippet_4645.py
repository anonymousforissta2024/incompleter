#Source: https://stackoverflow.com/questions/43880022/nameerror-name-sequences-is-not-defined
file_name = "chr21_dna_sequence.fasta"
read_fasta(file_name)
write_cat_seq(file_name, sequences)
print('Saved and Complete')