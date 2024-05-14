#Source: https://stackoverflow.com/questions/64265260/python-attributeerror-int-object-has-no-attribute-decode-when-trying-to-ca
import numpy as np
import networkx as nx

gml_path = "XXXX.gml"
gml_path = gml_path.encode("utf-8")
G = nx.read_gml(gml_path)
X = np.array(nx.to_numpy_matrix(G))
print(nx.is_directed(G))