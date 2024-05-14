#Source: https://stackoverflow.com/questions/60702740/attributeerror-module-networkx-has-no-attribute-generate-graph6
import networkx as nx
G=nx.Graph()
G.add_edges_from([(2, 3),(4, 5), (1, 3), (1, 2), (1, 5), (1, 4), (2, 4), (3, 5), (2, 5), (3, 4)])
nx.generate_graph6(G)