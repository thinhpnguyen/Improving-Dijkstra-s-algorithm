import heapq

class vertex:
    def __init__(self, name):
        self.name = str(name)
        self.adjacent = []                                          #[name of adjacent][weight]
        self.distance = 9999999
        self.isvisit = False
        self.previous = None

    def append_adjacent(self, node, distance):
        for i in range(len(self.adjacent)):
            if self.adjacent[i][0] == node:
                print("Vertex already existed.\n")
                return
        self.adjacent.append([node, float(distance)])

    def get_weight(self, node):
        for i in range(len(self.adjacent)):
            if self.adjacent[i][0] == node:
                return self.adjacent[i][1]                          #return adjecent distance
        return 0                                            #not exist

    def sort(self):                                                 #Insertion sort
        for i in range(1, len(self.adjacent)):
            key = self.adjacent[i][1]
            j = i - 1
            while j >= 0 and key < self.adjacent[j][1]:
                self.adjacent[j+1][1] = self.adjacent[j][1]
                j -= 1
                self.adjacent[j+1][1] = key
        return self.adjacent

    def is_connect(self, name):
        for i in range(0, len(self.adjacent)):
            if self.adjacent[i][0] == name:
                return True
        return False

    def reset_status(self):
        self.isvisit = False

    def visit_vertex(self):
        self.isvisit = True

    def set_distance(self, distance):
        self.distance = distance

    def get_distance(self):
        return self.distance

    def number_of_edge(self):
        return len(self.adjacent)

    def get_name(self):
        return self.name

    def set_previous(self, prev):
        self.previous = prev

    def is_visit(self):
        return self.isvisit

    def __lt__(self, other):
        pass

    def __le__(self, other):
        pass

class graph:
    def __init__(self):
        self.array = []
        self.path = []

    def add_vertex(self, vert):
        self.array.append(vert)

    def connect_2_direction(self, first: vertex, second: vertex, distance: float):
        first.append_adjacent(second, distance)
        second.append_adjacent(first, distance)

    def connect_1_direction(self, first: vertex, second: vertex, distance):
        first.append_adjacent(second, distance)

    def is_connect(self, first: vertex, second: vertex) -> bool:
        for i in range(0, len(self.array)):
            if self.array[i] == first:
                return self.array[i].is_connect(second)

    def get_weight(self, first: vertex, second: vertex) -> float:
        return first.get_weight(second)

    def shortest(self,target, path):
        path.append(target)
        if target.previous:
            self.shortest(target.previous, path)
        return

    def dijkstra(self, start: vertex):
        start.set_distance(0)
        unvisited_queue = [(int(v.get_distance()), v) for v in self.array]
        heapq.heapify(unvisited_queue)
        while len(unvisited_queue):
            uv = heapq.heappop(unvisited_queue)
            current = uv[1]
            current.visit_vertex()
            for next in current.adjacent:
                if next[0].is_visit():
                    continue
                new_dist = current.get_distance() + current.get_weight(next)

                if new_dist < next[0].get_distance():
                    next[0].set_distance(new_dist)
                    next[0].set_previous(current)
                else:
                    pass

            while len(unvisited_queue):
                heapq.heappop(unvisited_queue)
            unvisited_queue = [(int(v.get_distance()), v) for v in self.array if not v.isvisit]
            heapq.heapify(unvisited_queue)

if __name__ == "__main__":
    a = vertex("A")
    b = vertex("B")
    c = vertex("C")
    d = vertex("D")
    e = vertex("E")
    f = vertex("F")
    g = vertex("G")
    h = vertex("H")

    test_graph = graph()
    test_graph.add_vertex(a)
    test_graph.add_vertex(b)
    test_graph.add_vertex(c)
    test_graph.add_vertex(d)
    test_graph.add_vertex(e)
    test_graph.add_vertex(f)
    test_graph.add_vertex(g)
    test_graph.add_vertex(h)

    # test_graph.connect_2_direction(a, b, 10)
    #     # test_graph.connect_2_direction(a, c, 3)
    #     # test_graph.connect_2_direction(a, d, 8)
    #     # test_graph.connect_2_direction(b, c, 8)
    #     # test_graph.connect_2_direction(c, d, 4)
    #     # test_graph.connect_2_direction(b, e, 6)
    #     # test_graph.connect_2_direction(c, f, 9)
    #     # test_graph.connect_2_direction(d, g, 7)
    #     # test_graph.connect_2_direction(e, f, 3)
    #     # test_graph.connect_2_direction(f, g, 1)
    #     # test_graph.connect_2_direction(e, h, 11)
    #     # test_graph.connect_2_direction(f, h, 8)
    #     # test_graph.connect_2_direction(g, h, 5)

    test_graph.connect_1_direction(a, b, 7)
    test_graph.connect_1_direction(a, c, 9)
    test_graph.connect_1_direction(a, f, 14)
    test_graph.connect_1_direction(b, c, 10)
    test_graph.connect_1_direction(b, d, 15)
    test_graph.connect_1_direction(c, d, 11)
    test_graph.connect_1_direction(c, f, 2)
    test_graph.connect_1_direction(d, e, 6)
    test_graph.connect_1_direction(e, f, 9)

    print(test_graph.is_connect(a, d))
    print(test_graph.get_weight(a, c))
    test_graph.dijkstra(a)
    path = []
    test_graph.dijkstra(a)
    test_graph.shortest(e, path)
    for i in range(0, len(path)):
        print(path[i].name)
