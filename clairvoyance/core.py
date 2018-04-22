import networkx as nx

class Graph():
    def __init__(self):
        self.graph = nx.Graph()

    def add_entity(self, name, type):
        print(self.graph)
        self.graph.add_node(name, type = type)

    def make_transform(self, nodes, transform_function):
        flat_nodes = []
        flat_edges = []

        # Create list of new elements from the given transform under node
        transform_results, type = transform_function(self.graph, nodes)
        print('Transform results:', transform_results)
        # If the input was compatible
        if (transform_results != -1):
            # Add new nodes to the graph based on the transform results
            for item in transform_results:
                if isinstance(item, list):
                    flat_nodes.extend([subitem for subitem in item])
                else:
                    flat_nodes.extend([item])
            print('Flat nodes:', flat_nodes)
            self.graph.add_nodes_from(flat_nodes, type = type)

            # Add edges between the initial node and the new transform results
            for i in range(0, len(transform_results)):
                if isinstance(transform_results[i], list):
                    flat_edges.extend([(nodes[i], subitem) for subitem in transform_results[i]])
                else:
                    flat_edges.extend([(nodes[i], transform_results[i])])
            print(flat_edges)
            self.graph.add_edges_from(flat_edges)
