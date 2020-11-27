from ver import Vertex
import sys
import math

class graph:
    def __init__(self):
        self.vert_dict = {} #vertex dictionary
        self.num_vertices = 0
        self.num_edges = 0
    def __iter__(self):
        return iter(self.vert_dict.values())

    def add_vertex(self, node, x, y):
        #self.num_vertices += 1 # increment number of vertices
        new_vertex = Vertex(node, x, y)
        self.vert_dict[node] = new_vertex
        return new_vertex
    def get_vertex(self, n):
        if n in self.vert_dict:
            return self.vert_dict[n]
        else:
            return None

    def add_edge(self, frm, to):
        # if frm not in self.vert_dict:
        #     self.add_vertex(frm)
        # if to not in self.vert_dict:
        #     self.add_vertex(to)

        ver1 = self.get_vertex(frm)
        ver2 = self.get_vertex(to)
        cost = math.sqrt((ver1.x - ver2.x)**2 + (ver1.y - ver2.y)**2)
        self.vert_dict[frm].add_neighbor(self.vert_dict[to], cost)

    def get_vertices (self) :
        return self.vert_dict.keys()

    def set_previous(self, current):
        self.previous = current

    def get_previous(self, current):
        return self.previous



