import unittest
import io
import sys
from theq import node, displayGraph, to_mermaid, deleteGraph

# Run: python3 -m theq test -v

class TestNode(unittest.TestCase):
    def test_node_creation(self):
        n = node(5, None)
        self.assertEqual(n.vertex, 5)
        self.assertIsNone(n.next)
    
    def test_node_chaining(self):
        n2 = node(2, None)
        n1 = node(1, n2)
        self.assertEqual(n1.vertex, 1)
        self.assertIs(n1.next, n2)


class TestDisplayGraph(unittest.TestCase):
    def test_display_empty_vertex(self):
        Adj = [None]
        output = self._capture_output(lambda: displayGraph(Adj, 1))
        self.assertIn("—", output)
    
    def test_display_with_neighbors(self):
        Adj = [None] * 2
        Adj[0] = node(1, node(2, None))
        Adj[1] = None
        output = self._capture_output(lambda: displayGraph(Adj, 2))
        self.assertIn("-> 1", output)
        self.assertIn("-> 2", output)
    
    def test_display_multiple_vertices(self):
        Adj = [None] * 3
        Adj[0] = node(1, None)
        Adj[1] = None
        Adj[2] = node(0, None)
        output = self._capture_output(lambda: displayGraph(Adj, 3))
        self.assertIn("Node 0", output)
        self.assertIn("Node 1", output)
        self.assertIn("Node 2", output)
    
    def _capture_output(self, func):
        captured = io.StringIO()
        sys.stdout = captured
        func()
        sys.stdout = sys.__stdout__
        return captured.getvalue()


class TestToMermaid(unittest.TestCase):
    def test_mermaid_header_and_vertices(self):
        Adj = [None]
        result = to_mermaid(Adj, 1)
        self.assertTrue(result.startswith("graph TD"))
        self.assertIn("0", result)
    
    def test_mermaid_edges(self):
        Adj = [None] * 2
        Adj[0] = node(1, None)
        Adj[1] = None
        result = to_mermaid(Adj, 2)
        self.assertIn("0 --- 1", result)
    
    def test_mermaid_no_duplicate_reverse_edges(self):
        Adj = [None] * 2
        Adj[0] = node(1, None)
        Adj[1] = node(0, None)
        result = to_mermaid(Adj, 2)
        self.assertEqual(result.count("0 --- 1"), 1)


class TestDeleteGraph(unittest.TestCase):
    def test_delete_graph(self):
        Adj = [None] * 3
        Adj[0] = node(1, None)
        Adj[1] = node(2, None)
        Adj[2] = node(0, None)
        
        self._capture_output(lambda: deleteGraph(Adj, 3))
        
        for i in range(3):
            self.assertIsNone(Adj[i])
    
    def _capture_output(self, func):
        captured = io.StringIO()
        sys.stdout = captured
        func()
        sys.stdout = sys.__stdout__
        return captured.getvalue()


if __name__ == "__main__":
    unittest.main()
