#Source: https://stackoverflow.com/questions/51488228/attributeerror-str-object-has-no-attribute-id-using-biopython-parsing-fast
file_in ='lots_of_fasta_in_file.fasta'
file_out='new.fasta'

with open(file_out, 'w') as f_out:
    with open(file_in, 'r') as f_in:
        for seq_record in SeqIO.parse(f_in, 'fasta'):
            name, sequence = seq_record.id, str(seq_record.seq)
            # remove .seq from ID and add features
            pair = [name.replace('.seq',''), sequence]
            SeqIO.write(pair, file_out, 'fasta')