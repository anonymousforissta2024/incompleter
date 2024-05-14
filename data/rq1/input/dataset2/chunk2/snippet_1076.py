#Source: https://stackoverflow.com/questions/43356922/attributeerror-gzipfile-object-has-no-attribute-next
import gzip
import numpy as np

"""
Read in a SOFT format data file.  The following values can be exported:

GID : A list of gene identifiers of length d
SID : A list of sample identifiers of length n
STP : A list of sample descriptions of length d
X   : A dxn array of gene expression values
"""

fname = "../Anchang Charles/GDS1615_full.soft.gz"
with gzip.open(fname) as fid:
    SIF = {}
    for line in fid:
        if line.startswith(line, len("!dataset_table_begin")):
            break
        elif line.startswith(line, len("!subject_description")):
            subset_description = line.split("=")[1].strip()
        elif line.startswith(line, len("!subset_sample_id")):
            subset_ids = [x.strip() for x in subset_ids]
            for k in subset_ids:
                SIF[k] = subset_description
                  #.next().split("\t")
    SID = fid.next().split("\t")
    I = [i for i,x in enumerate(SID) if x.startswith("GSM")]
    SID = [SID[i] for i in I]
    STP = [SIF[k] for k in SID]