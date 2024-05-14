#Source: https://stackoverflow.com/questions/60029383/typeerror-not-supported-between-instances-of-dict-and-dict-python-3-co
nodes=random.randint(47,52)
p=random.uniform(0.05,0.08)
name="Erdos-Renyi random weighted graph"
G=nx.erdos_renyi_graph(nodes,p)
maxw=random.randint(7,12)
weight=weight_attr(G,maxw)
w_edges=[(x,y,z) for (x,y),z in weight.items()]
G.add_weighted_edges_from(w_edges)
G=nx.Graph(G,name=name)
print ("Graph G is a %s with %i nodes, p=%.3f and %i edges\n" %(str(G),len(G.nodes()),p,len(G.edges())))

res = list(sorted(Counter(G.edges()), key=Counter(G.edges()).__getitem__, reverse=True))
for i in res:
    print ("Edge", i, "has weight", Counter(G.edges())[i]['weight'])