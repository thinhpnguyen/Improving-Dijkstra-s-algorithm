from collections import defaultdict


class Graph:
    def __init__(self):
        self.edges = defaultdict(list)
        self.weights = {}

    def add_edge(self, from_node, to_node, weight):
        # connecting nodes from both sides
        self.edges[from_node].append(to_node)
        self.edges[to_node].append(from_node)
        # catering for the source and destination nodes
        self.weights[(from_node, to_node)] = weight
        self.weights[(to_node, from_node)] = weight
        # combining the indegree and outdegree weights were possible
        

def dijsktra(graph, initial, end):
    # the shortest paths is a dict of nodes
    # whose value is a tuple of (previous node, weight)
    shortest_paths = {initial: (None, 0)}
    current_node = initial
    visited = set()

    while current_node != end:
        visited.add(current_node)
        destinations = graph.edges[current_node]
        weight_to_current_node = shortest_paths[current_node][1]

        for next_node in destinations:
            weight = graph.weights[(current_node, next_node)] + weight_to_current_node
            if next_node not in shortest_paths:
                shortest_paths[next_node] = (current_node, weight)
            else:
                current_shortest_weight = shortest_paths[next_node][1]
                if current_shortest_weight > weight:
                    shortest_paths[next_node] = (current_node, weight)

        next_destinations = {node: shortest_paths[node] for node in shortest_paths if node not in visited}
        if not next_destinations:
            return "Route Not Possible"
        # the next node is the destination with the lowest weight
        current_node = min(next_destinations, key=lambda k: next_destinations[k][1])

    # determing the shortest path
    path = []
    while current_node is not None:
        path.append(current_node)
        next_node = shortest_paths[current_node][0]
        current_node = next_node
    # Reverse path
    path = path[::-1]
    return path


g = Graph()

edges = [
("A", "B", 10),
("A", "C", 3),
("A", "D", 8),
("B", "C", 8),
("C", "D", 4),
("B", "E", 6),
("C", "F", 9),
("D", "G", 7),
("E", "F", 3),
("F", "G", 1),
("E", "H", 11),
("F", "H", 8),
("G", "H", 5)]

for edge in edges:
    g.add_edge(*edge)

print(dijsktra(g,"A","E"))