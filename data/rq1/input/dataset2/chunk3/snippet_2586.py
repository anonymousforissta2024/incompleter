#Source: https://stackoverflow.com/questions/58225629/typeerror-in-python-3
class TSP:
    def __init__(self, initial_node, adjacency_matrix):
        self.initial_node = initial_node
        self.adjacency_matrix = adjacency_matrix

    stack = {"cost": {}, "distances": {}}

    def distance(self, start_node, end_node):
        self.stack["distances"]["dist%s-%s" %(start_node, end_node)] = self.adjacency-matrix[start_node][end_node]

    def cost(self, visit_nodes, end_node_cost):
        if len(visit_nodes) == 2:
            node_set = visit_nodes.remove(end_node_cost)
            self.distance(node_set[0], end_node_cost)
        print (self.stack)


test = TSP(1, [[0, 10, 15, 20], [10, 0, 35, 25], [15, 35, 0, 30], [20, 25, 30, 0]])

print (test.cost([1, 2], 2))