import heapq
from graph import graph
import sys
import math
import time
import random


def shortest(v, path):
    ''' make shortest path from v.previous'''
    if v.previous:
        path.append(v.previous.get_id())
        shortest(v.previous, path)
    return

def re_initialize(list):
    for i in list:
        i.distance = sys.maxsize
        i.previous = None
        i.visited = False
        i.dtod = sys.maxsize
def dist(one, two):
    return math.sqrt((one.x - two.x)**2 + (one.y - two.y)**2) # distance of two points in 2D


def dijkstra (G, start, target):
    # G.re_initialize()  # reset all vertices' distance to infinity and delete all path
    start.set_distance(dist(start, target)) # set to the distance of source to sink to not get negative when calculating distances if adjacents
    start.set_dtd(dist(start, target))
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
                next.set_dtd(dist(next, target)) # only calculate dtd for the add vertices
            new_dist = current.get_distance() + current.get_weight(next) + next.get_dtd() + current.get_dtd()  # also add in Euclidean distance to make it goes to the distance of the sink
            if new_dist < next.get_distance():  # update distance when smaller path is available
                next.set_distance(new_dist)
                next.set_previous(current)
                # print('updated : current = %s next = %s new_dist = %s' \  #print out process
                # % (current.get_id(), next.get_id(), next.get_distance()))
            else:
                continue
                # print('not updated : current = %s next = %s new_dist = %s' \
                # % (current.get_id(), next.get_id(), next.get_distance()))
        heapq.heapify(unvisited_queue) # heapify the queue again

    # print out the path
    if target.distance is sys.maxsize: # if distance of target is infinity => not connected to source
         print("No Path!")
    else:
         path = [target.get_id()] # path is a list
         shortest(target, path)
         print('The shortest path : %s' %(path[::-1]))
    re_initialize(visited_list)  # IMPROVEMENT #2: only reinitialize the vertices that changed
    #print("Done!")

def test():
    size = 8000
    t0 = time.time()
    for i in range(10):
        r1 = random.randint(0, size)
        r2 = random.randint(0, size)
        dijkstra(g, g.get_vertex(str(r1)), g.get_vertex(str(r2)))
    t1 = time.time()
    return t1 - t0

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

    # test sigal querry
    # t1=time.time()
    dijkstra(g, g.get_vertex('0'), g.get_vertex('100'))
    # t2=time.time()
    # print("The time is: ")
    # print(t2 - t1)

    # test average
    # total = 0
    # times = 10
    # for i in range(times):
    #     total += test()
    # print("Average is: ")
    # print(total/times)

