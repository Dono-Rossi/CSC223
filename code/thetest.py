import unittest
import io
import sys
from theq import node, displayGraph, to_mermaid, deleteGraph

# Run: python3 -m theq thetest -v

class TestNode(unittest.TestCase):
    def test_node_creation(self):
        n = node(5, None)
        self.assertEqual(n.vertex, 5)
        self.assertIsNone(n.next)
    
    def test_node_linking(self):
        n2 = node(2, None)
        n1 = node(1, n2)
        self.assertEqual(n1.vertex, 1)
        self.assertIs(n1.next, n2)


class TestDisplayGraph(unittest.TestCase):
    def test_display_empty(self):
        Adj = [None]
        output = self._get_output(displayGraph, Adj, 1)
        self.assertIn("—", output)
    
    def test_display_with_edges(self):
        Adj = [None, None]
        Adj[0] = node(1, node(2, None))
        Adj[1] = None
        output = self._get_output(displayGraph, Adj, 2)
        self.assertIn("-> 1", output)
        self.assertIn("-> 2", output)
    
    def test_display_multiple_vertices(self):
        Adj = [None, None, None]
        Adj[0] = node(1, None)
        Adj[1] = None
        Adj[2] = node(0, None)
        output = self._get_output(displayGraph, Adj, 3)
        self.assertIn("Node 0", output)
        self.assertIn("Node 1", output)
        self.assertIn("Node 2", output)
    
    def _get_output(self, func, adj, num):
        old_stdout = sys.stdout
        sys.stdout = io.StringIO()
        func(adj, num)
        result = sys.stdout.getvalue()
        sys.stdout = old_stdout
        return result


class TestToMermaid(unittest.TestCase):
    def test_mermaid_starts_correct(self):
        Adj = [None]
        result = to_mermaid(Adj, 1)
        self.assertTrue(result.startswith("graph TD"))
    
    def test_mermaid_has_vertex(self):
        Adj = [None]
        result = to_mermaid(Adj, 1)
        self.assertIn("0", result)
    
    def test_mermaid_shows_edge(self):
        Adj = [None, None]
        Adj[0] = node(1, None)
        Adj[1] = None
        result = to_mermaid(Adj, 2)
        self.assertIn("0 --- 1", result)
    
    def test_mermaid_no_duplicates(self):
        Adj = [None, None]
        Adj[0] = node(1, None)
        Adj[1] = node(0, None)
        result = to_mermaid(Adj, 2)
        count = result.count("0 --- 1")
        self.assertEqual(count, 1)


class TestDeleteGraph(unittest.TestCase):
    def test_delete_removes_edges(self):
        Adj = [None, None, None]
        Adj[0] = node(1, None)
        Adj[1] = node(2, None)
        Adj[2] = node(0, None)
        
        old_stdout = sys.stdout
        sys.stdout = io.StringIO()
        deleteGraph(Adj, 3)
        sys.stdout = old_stdout
        
        for i in range(3):
            self.assertIsNone(Adj[i])


if __name__ == "__main__":
    unittest.main()
