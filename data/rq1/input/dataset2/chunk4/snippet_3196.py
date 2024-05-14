#Source: https://stackoverflow.com/questions/65377587/what-i-have-the-erroe-typeerror-string-indices-must-be-integers-how-can-i-sol
pep = 'MEGNCS'
newseqs = []
bt= {'I': ['ATA', 'ATC', 'ATT'], 'M': ['ATG'], 'T': ['ACA', 'ACC', 'ACG', 'ACT'], 'N': ['AAC', 'AAT'], 'K': ['AAA', 'AAG'], 'S': ['AGC', 'AGT', 'TCA', 'TCC', 'TCG', 'TCT'], 'R': ['AGA', 'AGG', 'CGA', 'CGC', 'CGG', 'CGT'], 'L': ['CTA', 'CTC', 'CTG', 'CTT', 'TTA', 'TTG'], 'P': ['CCA', 'CCC', 'CCG', 'CCT'], 'H': ['CAC', 'CAT'], 'Q': ['CAA', 'CAG'], 'V': ['GTA', 'GTC', 'GTG', 'GTT'], 'A': ['GCA', 'GCC', 'GCG', 'GCT'], 'D': ['GAC', 'GAT'], 'E': ['GAA', 'GAG'], 'G': ['GGA', 'GGC', 'GGG', 'GGT'], 'F': ['TTC', 'TTT'], 'Y': ['TAC', 'TAT'], '_': ['TAA', 'TAG', 'TGA'], 'C': ['TGC', 'TGT'], 'W': ['TGG']}
back_trans(pep,bt, 0, newseqs)
print('\n'.join(newseqs))