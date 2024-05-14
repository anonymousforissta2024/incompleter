#Source: https://stackoverflow.com/questions/76737790/filenotfounderror-using-gcsfs-and-pandas-but-only-on-my-machine
import gcsfs
import pandas as pd
x = pd.read_table("gs://MYBUCKET/clinvar/gene_specific_summary.txt")