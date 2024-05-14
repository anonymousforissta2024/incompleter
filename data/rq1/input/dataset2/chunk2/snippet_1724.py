#Source: https://stackoverflow.com/questions/75897778/attributeerror-module-networkx-has-no-attribute-info
import networkx as nx
G = nx.read_edgelist('webpages.txt', create_using=nx.DiGraph())
print(nx.info(G))