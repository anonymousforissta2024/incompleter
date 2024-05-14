#Source: https://stackoverflow.com/questions/53017174/attributeerror-module-networkx-algorithms-community-has-no-attribute-best-pa
import networkx as nx
import matplotlib.pyplot as plt
from networkx.algorithms import community
from networkx.algorithms.community.centrality import girvan_newman

G_fb = nx.read_edgelist("./facebook_combined.txt",create_using = nx.Graph(), nodetype=int)

parts = community.best_partition(G_fb)
values = [parts.get(node) for node in G_fb.nodes()]