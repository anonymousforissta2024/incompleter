#Source: https://stackoverflow.com/questions/51488228/attributeerror-str-object-has-no-attribute-id-using-biopython-parsing-fast
with open ('lots_of_fasta_in_file.fasta') as f:
    for seq_record in SeqIO.parse(f, 'fasta'):
        name, sequence = seq_record.id, str(seq_record.seq)
        pair = [name.replace('.seq',''), sequence]
        SeqIO.write(pair, "new.fasta", "fasta")