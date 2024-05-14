#Source: https://stackoverflow.com/questions/51991264/typeerror-edges-takes-no-keyword-arguments
import csv
from collections import defaultdict
from typing import Dict, Any
import pandas as pd
from IPython.utils import data
from networkit import *
import numpy as np
import networkx as nx
from networkit.graphio import GraphConverter
from numpy import genfromtxt
import metis as mt
from networkx.utils import make_str
from _NetworKit import Graph

df1 = pd.read_csv ( 'person_knows_person_0_0.csv', sep='|', index_col=False )
df2 = pd.DataFrame ( df1 )
src_list = df2[':START_ID(Person)'].values.tolist ()
tgt_list = df2[':END_ID(Person)'].values.tolist ()

print ( src_list[1] )
print ( tgt_list[1] )
f = open ( 'sample_ex.csv', 'w' )
for (src, tgt) in zip ( src_list, tgt_list ):
    f.write ( str ( src ) + ',' + str ( tgt ) + '\n' )
f.close ()
reader = graphio.EdgeListReader ( ',', 1, continuous=False )
G = reader.read ( 'sample_ex.csv' )
print ( G )
graphio.writeGraph ( G, 'newgraph.graph', Format.METIS )
metisgraph = graphio.readGraph ( "newgraph.graph", Format.METIS )
print ( metisgraph )
G.indexEdges ()
print ( "Original size: ", G.size () )

sparsificationAlgorithm = sparsification.LocalDegreeSparsifier ()
S = sparsificationAlgorithm.getSparsifiedGraph ( G, 0.5 )
print ( "Sparsified size: ", S.size () )


nx.write_edgelist(S, 'sparsified_graph.edgelist', ',')