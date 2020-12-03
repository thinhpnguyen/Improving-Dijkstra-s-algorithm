import heapq
from graph import graph
import sys
import math
import time
import random
import io


def shortest(v, path):
    ''' make shortest path from v.previous'''
    while v.previous is not None:
        path.append(v.previous.get_id())
        v = v.previous
    return

def re_initialize(list):
    for i in list:
        i.distance = sys.maxsize
        i.previous = None
        i.visited = False
def dist(one, two):
    return math.sqrt((one.x - two.x)**2 + (one.y - two.y)**2) # distance of two points in 2D


def dijkstra (start, target):
    # G.re_initialize()  # reset all vertices' distance to infinity and delete all path
    start.dtd = dist(start, target)
    start.set_distance(start.get_dtd()) # set to the distance of source to its dtd
    unvisited_queue = []
    visited_list = [] # keep track of all vertices that changed
    unvisited_queue.append([start.get_distance(), start]) # add the source to the queue first
    start.visited = True
    visited_list.append(start)
    while len(unvisited_queue):
        uv = heapq.heappop(unvisited_queue) # get the one with least shortest distance to source
        if uv[1] is target:
            break  # IMPROVEMENT #1: break when the target is found
        current = uv[1]  # set to the node of the current vertex

        for next in current.adjacent:
            if not next.visited:  # only add the vertices that not already on the queue or not popped from queue
                unvisited_queue.append([next.get_distance(), next])  # add the adjacent to queue
                next.visited = True
                visited_list.append(next)
                next.dtd = dist(next, target) # only have to calculate dtd once
            new_dist = current.get_distance() + current.get_weight(next) + next.get_dtd() - current.get_dtd() # also add in Euclidean distance to make it goes to the direction of the sink
            if new_dist < next.get_distance():  # update distance when smaller path is available
                next.set_distance(new_dist)
                next.set_previous(current)
            else:
                continue
        # heapify the queue again
        heapq.heapify(unvisited_queue)

    # print out the path
    if target.distance is sys.maxsize: # if distance of target is infinity => not connected to source
        print("No Path!")
    else:
        path = [target.get_id()] # path is a list
        shortest(target, path)
        print('The shortest path : %s' %(path[::-1]))
        del path
    re_initialize(visited_list)  # IMPROVEMENT #2: only reinitialize the vertices that changed

def sample_test(di):
    size = 87575
    t0 = time.time()
    suppress_text = io.StringIO()
    sys.stdout = suppress_text
    print("Time test start.")
    test_size = 750
    for i in range(test_size):
        r1 = random.randint(0, size - 1)
        r2 = random.randint(0, size - 1)
        di( g.get_vertex(str(r1)), g.get_vertex(str(r2)))
    t1 = time.time()
    sys.stdout = sys.__stdout__
    return (t1 - t0)/test_size

if __name__ == '__main__':

    g = graph()

    # g.add_vertex('a')
    # g.add_vertex('b')
    # g.add_vertex('c')
    # g.add_vertex('d')
    # g.add_vertex('e')
    # g.add_vertex('f')
    #
    # g.add_edge('a', 'b', 7)
    # g.add_edge('a', 'c', 9)
    # g.add_edge('a', 'f', 14)
    # g.add_edge('b', 'c', 10)
    # g.add_edge('b', 'd', 15)
    # g.add_edge('c', 'd', 11)
    # g.add_edge('c', 'f', 2)
    # g.add_edge('d', 'e', 6)
    # g.add_edge('e', 'f', 9)

    with open('usa.txt', 'r') as file:
        # reading each line
        count = 0
        for line in file:
            if count == 0:
                # reading # of vertices and # of edges
                num_vertices, num_edges = line.split()
                g.num_vertices = int(num_vertices)
                g.num_edges = int(num_edges)
                count += 1
                continue
            if count > 0 and count < (g.num_vertices + 1):
                name, x, y = line.split()
                g.add_vertex(name, x, y)
                count += 1
                continue
            if count > g.num_vertices:
                name1, name2 = line.split()
                name3 = name2.rstrip('\n')
                g.add_edge(name1, name3)
                count += 1
                continue
    # for v in g:
    #     for w in v.get_connections():
    #         vid = v.get_id()
    #         wid = w.get_id()
    #         print('( %s , %s, %s)'  % ( vid, wid, v.get_weight(w)))

    # t0 = time.time()
    #dijkstra(g, g.get_vertex('0'), g.get_vertex('105'))
    # t1 = time.time()
    # print(t1 - t0)
    # print("Time test start.")
    # total = 0
    # times = 5
    # for i in range(times):
    #     total += sample_test(dijkstra)
    # print("Average is: ")
    # print(total/times)
    avg = sample_test(dijkstra)
    print(avg)