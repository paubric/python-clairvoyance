import networkx as nx

class Graph():
    def __init__(self):
        self.graph = nx.Graph()

    def add_entity(self, name, type):
        print(self.graph)
        self.graph.add_node(name, type = type)

    def make_transform(self, nodes, transform_function):
        # Create list of new elements from the given transform under node
        transform_results, type = transform_function(self.graph, nodes)

        # If the input was compatible
        if (transform_results != -1):
            # Add new nodes to the graph based on the transform results
            self.graph.add_nodes_from(transform_results, type = type)

            # Add edges between the initial node and the new transform results
            self.graph.add_edges_from([(node, result) for result in transform_results for node in nodes])
