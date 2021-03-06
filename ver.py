import sys

class Vertex:
    def __init__(self, node, long, lat):
        self.id = node
        self.adjacent = {}
        # Set distance to infinity for all nodes
        self.distance = sys.maxsize
        # Mark all nodes unvisited
        self.visited = False
        # Predecessor
        self.previous = None
        self.x = float(long)
        self.y = float(lat)
        self.dtd = sys.maxsize # Euclidean distance to sink

    def __gt__(self, b):  # has to overload greater than operator for heapd
        return self.distance > b.distance

    def add_neighbor(self, neighbor, weight=0.0):
        self.adjacent[neighbor] = float(weight)   # key is the vertex name

    def get_connections(self):
        return self.adjacent.keys()

    def get_id(self):
        return self.id

    def get_weight(self, neighbor):
        return float(self.adjacent[neighbor])

    def set_distance(self, dist):
        self.distance = dist

    def get_distance(self):
        return self.distance

    def get_dtd(self):
        return self.dtd

    def set_previous(self, prev):
        self.previous = prev

    def set_visited(self):
        self.visited = True

    def set_dtd(self, dis):
        self.dtd = dis

    def __str__(self):
        return str(self.id) + ' adjacent: ' + str([x.id for x in self.adjacent])