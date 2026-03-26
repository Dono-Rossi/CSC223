import unittest
from graphs import Graph

class TestGraphInit(unittest.TestCase):
# Tests that __init__ correctly sets up a new Graph's internal state.
    def test_correct_vertex_count(self):
        # Verifies num_vertices is stored as-is and not discarded.
        g = Graph(5)
        self.assertEqual(g.num_vertices, 5)
    def test_adj_keys_match_vertices(self):
        # adj must have exactly one key per vertex (0 through num_vertices-1).
        # Set comparison ignores insertion order.
        g = Graph(4)
        self.assertEqual(set(g.adj.keys()), {0, 1, 2, 3})
    def test_adj_lists_start_empty(self):
        # Every vertex's neighbor list must be [] on construction.
        # Iterates all values so a bug affecting only certain indices can't slip through.
        g = Graph(3)
        for neighbors in g.adj.values():
            self.assertEqual(neighbors, [])
    def test_zero_vertices(self):
        # A 0-vertex graph is a valid edge case; adj must be completely empty.
        g = Graph(0)
        self.assertEqual(g.num_vertices, 0)
        self.assertEqual(g.adj, {})

class TestAddNeighbors(unittest.TestCase):
# Tests that add_neighbors appends to the target vertex without disturbing others.
    def test_add_single_neighbor(self):
        # Smoke test: one neighbor must appear in the target vertex's list.
        g = Graph(3)
        g.add_neighbors(0, [1])
        self.assertIn(1, g.adj[0])
    def test_add_multiple_neighbors(self):
        # All neighbors must be stored and in the original order.
        g = Graph(4)
        g.add_neighbors(2, [0, 1, 3])
        self.assertEqual(g.adj[2], [0, 1, 3])
    def test_add_neighbors_twice_extends(self):
        # Two calls on the same vertex must accumulate, not replace.
        g = Graph(3)
        g.add_neighbors(0, [1])
        g.add_neighbors(0, [2])
        self.assertEqual(g.adj[0], [1, 2])
    def test_add_empty_neighbors(self):
        # Passing [] must be a no-op; the list must stay empty.
        g = Graph(2)
        g.add_neighbors(0, [])
        self.assertEqual(g.adj[0], [])
    def test_other_vertices_unaffected(self):
        # Modifying vertex 0 must not touch vertices 1 or 2.
        # Catches shared-reference bugs common with mutable defaults.
        g = Graph(3)
        g.add_neighbors(0, [1, 2])
        self.assertEqual(g.adj[1], [])
        self.assertEqual(g.adj[2], [])
    def test_duplicate_neighbors_allowed(self):
        # Graph uses a list, not a set, so duplicates must be preserved.
        g = Graph(3)
        g.add_neighbors(0, [1, 1])
        self.assertEqual(g.adj[0], [1, 1])

class TestDelete(unittest.TestCase):
# Tests that delete() wipes all adjacency data, leaving self.adj as {}.
    def test_adj_empty_after_delete(self):
        # After delete(), self.adj must have no keys at all.
        g = Graph(3)
        g.add_neighbors(0, [1, 2])
        g.delete()
        self.assertEqual(g.adj, {})
    def test_delete_on_empty_graph(self):
        # delete() on a 0-vertex graph must not raise.
        g = Graph(0)
        g.delete()
        self.assertEqual(g.adj, {})
    def test_double_delete(self):
        # A second delete() on an already-deleted graph must be safe.
        g = Graph(2)
        g.add_neighbors(0, [1])
        g.delete()
        g.delete()
        self.assertEqual(g.adj, {})

class TestDisplay(unittest.TestCase):
# Tests display() output by capturing stdout with io.StringIO.
    def test_display_with_neighbors(self):
        # Output must reference both the vertex label and its neighbor.
        # assertIn avoids brittleness against minor formatting changes.
        g = Graph(2)
        g.add_neighbors(0, [1])
        import io, sys
        captured = io.StringIO()
        sys.stdout = captured
        g.display()
        sys.stdout = sys.__stdout__
        output = captured.getvalue()
        self.assertIn("0", output)
        self.assertIn("1", output)
    def test_display_no_neighbors_shows_none(self):
        # When a vertex has no neighbors, "(none)" must appear in the output.
        g = Graph(1)
        import io, sys
        captured = io.StringIO()
        sys.stdout = captured
        g.display()
        sys.stdout = sys.__stdout__
        output = captured.getvalue()
        self.assertIn("(none)", output)


if __name__ == "__main__":
    unittest.main()
