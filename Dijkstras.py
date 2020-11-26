import heapq
from graph import graph


def shortest(v, path):
    ''' make shortest path from v.previous'''
    if v.previous:
        path.append(v.previous.get_id())
        shortest(v.previous, path)
    return


def dijkstra (G, start, target):
    G.re_initialize()  # reset all vertices' distance to infinity and delete all path
    start.set_distance(0)
    unvisited_queue = []
    unvisited_queue.append([start.get_distance(), start]) # add the source to the queue first
    while len(unvisited_queue):
        uv = heapq.heappop(unvisited_queue) # get the one with least shortest distance to source

        if not uv[1].visited:
            uv[1].visited = True

        if uv is target:
            break  # first improvement: break when the target is found
        current = uv[1]  # set to the node of the current vertex

        for next in current.adjacent:
            if not next.visited or not next.added:  # only add the vertices that not already on the queue or not popped from queue
                unvisited_queue.append([next.get_distance(), next])  # add the adjacent to queue
                next.added = True
            new_dist = current.get_distance() + current.get_weight(next)  # will improve here

            if new_dist < next.get_distance():  # update distance when smaller path is available
                next.set_distance(new_dist)
                next.set_previous(current)
            else:
                continue
        # heapify the queue again
        heapq.heapify(unvisited_queue)

    # print out the path
    path = [target.get_id()]
    shortest(target, path)
    print('The shortest path : %s' %(path[::-1]))


if __name__ == '__main__':

    g = graph()

    g.add_vertex('a')
    g.add_vertex('b')
    g.add_vertex('c')
    g.add_vertex('d')
    g.add_vertex('e')
    g.add_vertex('f')

    g.add_edge('a', 'b', 7)
    g.add_edge('a', 'c', 9)
    g.add_edge('a', 'f', 14)
    g.add_edge('b', 'c', 10)
    g.add_edge('b', 'd', 15)
    g.add_edge('c', 'd', 11)
    g.add_edge('c', 'f', 2)
    g.add_edge('d', 'e', 6)
    g.add_edge('e', 'f', 9)

    for v in g:
        for w in v.get_connections():
            vid = v.get_id()
            wid = w.get_id()
            print('( %s , %s, %3d)'  % ( vid, wid, v.get_weight(w)))

    dijkstra(g, g.get_vertex('a'), g.get_vertex('e'))
    dijkstra(g, g.get_vertex('d'), g.get_vertex('f'))
