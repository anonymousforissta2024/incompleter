#Source: https://stackoverflow.com/questions/75565224/in-pyvis-i-always-get-this-error-attributeerror-nonetype-object-has-no-attr
from pyvis.network import Network
g = Network()
g.add_node(0)
g.add_node(1)
g.add_edge(0, 1)
g.show('test.html')