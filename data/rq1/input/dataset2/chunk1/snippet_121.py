#Source: https://stackoverflow.com/questions/40069585/how-can-i-fix-attributeerror-dict-values-object-has-no-attribute-count
import networkx as nx
import pylab as plt

webg = nx.read_edgelist('web-graph.txt',create_using=nx.DiGraph(),nodetype=int)
in_degrees = webg.in_degree()
in_values = sorted(set(in_degrees.values()))
in_hist = [in_degrees.values().count(x)for x in in_values]