class vertex:
    def __init__(self, name):
        self.name = str(name)
        self.adjacent = []                                          #[name of adjacent][weight][Is visited]
        self.distance = 9999999

    def append_adjacent(self, name, distance):
        for i in range(len(self.adjacent)):
            if self.adjacent[i][0] == name:
                print("Vertex already existed.\n")
                return
        self.adjacent.append([str(name), float(distance), False])
        self.sort()

    def get_weight(self, name):
        for i in range(len(self.adjacent)):
            if self.adjacent[i][0] == name:
                return self.adjacent[i][1]                          #return adjecent distance
            else:
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
        for i in range(0, len(self.adjacent)):
            self.adjacent[i][2] = False

    def visit_vertex(self, number):
        self.adjacent[number][2] = True
        return [self.adjacent[number][0], self.adjacent[number][1]]         #return array with name and weight

    def set_distance(self, distance):
        self.distance = distance

    def get_distance(self):
        return self.distance

    def number_of_edge(self):
        return len(self.adjacent)

    def get_name(self):
        return self.name