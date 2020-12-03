import unittest
from graph import *
from Dijkstras import *
import math
from ver import *
import sys
import contextlib
from io import *

def captured_output():
    new_out, new_err = StringIO(), StringIO()
    old_out, old_err = sys.stdout, sys.stderr
    try:
        sys.stdout, sys.stderr = new_out, new_err
        yield sys.stdout, sys.stderr
    finally:
        sys.stdout, sys.stderr = old_out, old_err

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)

    # 0|| 1 || 2 || 3 || 4 || 5 || 6 || 7 || 8 || 9 || 10 ||
    # 1||   ||   ||   || b ||   || d ||   ||   ||   ||    ||
    # 2||   || a ||   ||   ||   ||   ||   || f ||   ||    ||
    # 3||   ||   ||   || c ||   || e ||   ||   ||   ||    ||
    # 4||   ||   ||   ||   ||   ||   ||   ||   ||   ||    ||

    def test_vertex_existence(self):
        g = graph()
        g.add_vertex('a', 2, 2)
        g.add_vertex('b', 4, 1)
        g.add_vertex('c', 4, 3)
        g.add_vertex('d', 6, 1)
        g.add_vertex('e', 6, 3)
        g.add_vertex('f', 8, 2)

        self.assertEqual(g.get_vertex('a').get_id(), 'a')
        self.assertEqual(g.get_vertex('a').x, 2)
        self.assertEqual(g.get_vertex('a').y, 2)

        self.assertEqual(g.get_vertex('b').get_id(), 'b')
        self.assertEqual(g.get_vertex('b').x, 4)
        self.assertEqual(g.get_vertex('b').y, 1)

        self.assertEqual(g.get_vertex('c').get_id(), 'c')
        self.assertEqual(g.get_vertex('c').x, g.get_vertex('b').x)
        self.assertEqual(g.get_vertex('c').y, 3)

        self.assertEqual(g.get_vertex('d').get_id(), 'd')
        self.assertEqual(g.get_vertex('d').x, 6)
        self.assertEqual(g.get_vertex('d').y, 1)

        self.assertEqual(g.get_vertex('e').get_id(), 'e')
        self.assertEqual(g.get_vertex('e').x, g.get_vertex('d').x)
        self.assertEqual(g.get_vertex('e').y, 3)

        self.assertEqual(g.get_vertex('f').get_id(), 'f')
        self.assertEqual(g.get_vertex('f').x, 8)
        self.assertEqual(g.get_vertex('f').y, g.get_vertex('a').y)

        self.assertFalse(g.get_vertex('f').visited)
        g.get_vertex('f').set_visited()
        self.assertTrue(g.get_vertex('f').visited)

    def test_vertex_connection(self):
        g = graph()
        g.add_vertex('a', 2, 2)
        g.add_vertex('b', 4, 1)
        g.add_vertex('c', 4, 3)
        g.add_vertex('d', 6, 2)
        g.add_vertex('e', 6, 3)
        g.add_vertex('f', 8, 2)

        g.add_edge('a', 'b')
        g.add_edge('a', 'c')
        g.add_edge('b', 'd')
        g.add_edge('b', 'c')
        g.add_edge('c', 'd')
        g.add_edge('c', 'e')
        g.add_edge('e', 'd')
        g.add_edge('d', 'f')
        g.add_edge('e', 'f')
        a = g.get_vertex('a')
        b = g.get_vertex('b')
        d = g.get_vertex('d')
        self.assertIsNone(a.previous)
        self.assertEqual(a.get_weight(b), math.sqrt((a.x - b.x)**2 + (a.y - b.y)**2), math.sqrt((2 - 4)**2 + (2 - 1)**2))
        self.assertEqual(b.get_weight(d), math.sqrt((b.x - d.x) ** 2 + (b.y - d.y) ** 2), math.sqrt((4 - 6) ** 2 + (1 - 3) ** 2))

        temp_stdout = StringIO()
        with contextlib.redirect_stdout(temp_stdout):
            print(a)
        output = temp_stdout.getvalue().strip()
        self.assertEqual(output, "a adjacent: ['b', 'c']")

        temp_stdout = StringIO()
        with contextlib.redirect_stdout(temp_stdout):
            print(b)
        output = temp_stdout.getvalue().strip()
        self.assertEqual(output, "b adjacent: ['d', 'c']")

    # 0|| 1 || 2 || 3 || 4 || 5 || 6 || 7 || 8 || 9 || 10 ||
    # 1||   ||   ||   || b ||   || d ||   ||   ||   ||    ||
    # 2||   || a ||   ||   ||   ||   ||   || f ||   ||    ||
    # 3||   ||   ||   ||   ||   ||   ||   ||   ||   ||    ||
    # 4||   ||   ||   || c ||   ||   || e ||   ||   ||    ||

    def test_sorted_path(self):
        g = graph()
        g.add_vertex('a', 2, 2)
        g.add_vertex('b', 4, 1)
        g.add_vertex('c', 4, 4)
        g.add_vertex('d', 6, 1)
        g.add_vertex('e', 7, 4)
        g.add_vertex('f', 8, 2)

        g.add_edge('a', 'b')
        g.add_edge('a', 'c')
        g.add_edge('b', 'c')
        g.add_edge('c', 'd')
        g.add_edge('c', 'e')
        g.add_edge('e', 'd')
        g.add_edge('d', 'f')
        g.add_edge('e', 'f')

        temp_stdout = StringIO()
        with contextlib.redirect_stdout(temp_stdout):
            dijkstra(g.get_vertex('a'), g.get_vertex('f'))
        output = temp_stdout.getvalue().strip()
        self.assertEqual(output, "The shortest path : ['a', 'c', 'e', 'f']")

        temp_stdout = StringIO()
        with contextlib.redirect_stdout(temp_stdout):
            dijkstra(g.get_vertex('b'), g.get_vertex('f'))
        output = temp_stdout.getvalue().strip()
        self.assertEqual(output, "The shortest path : ['b', 'c', 'e', 'f']")


if __name__ == '__main__':
    unittest.main()