import unittest
import io
import sys
from theq import node, displayGraph, to_mermaid, deleteGraph


class TestNode(unittest.TestCase):
    def test_node_initialization(self):
        n = node(5, None)
        self.assertEqual(n.vertex, 5)
        self.assertIsNone(n.next)
    
    def test_node_linking(self):
        n2 = node(2, None)
        n1 = node(1, n2)
        self.assertIs(n1.next, n2)


class TestDisplayGraph(unittest.TestCase):
    def test_display_basic_structure(self):
        Adj = [None] * 2
        Adj[0] = node(1, None)
        Adj[1] = None
        
        output = self._capture_display(Adj, 2)
        
        self.assertIn("Node 0", output)
        self.assertIn("-> 1", output)
        self.assertIn("Node 1", output)
        self.assertIn("—", output)
    
    def test_display_linked_chain(self):
        Adj = [None] * 3
        Adj[0] = node(1, node(2, None))
        Adj[1] = None
        Adj[2] = None
        
        output = self._capture_display(Adj, 3)
        
        self.assertIn("-> 1", output)
        self.assertIn("-> 2", output)
    
    def _capture_display(self, adj, nodenum):
        captured = io.StringIO()
        sys.stdout = captured
        displayGraph(adj, nodenum)
        sys.stdout = sys.__stdout__
        return captured.getvalue()


class TestToMermaid(unittest.TestCase):
    def test_mermaid_basic(self):
        Adj = [None] * 2
        Adj[0] = node(1, None)
        Adj[1] = None
        
        result = to_mermaid(Adj, 2)
        
        self.assertTrue(result.startswith("graph TD"))
        self.assertIn("0 --- 1", result)
    
    def test_mermaid_deduplicates_reverse_edges(self):
        Adj = [None] * 2
        Adj[0] = node(1, None)
        Adj[1] = node(0, None)
        
        result = to_mermaid(Adj, 2)
        
        # Should appear exactly once despite bidirectional edges
        self.assertEqual(result.count("0 --- 1"), 1)


class TestDeleteGraph(unittest.TestCase):
    def test_delete_clears_graph(self):
        Adj = [None] * 3
        Adj[0] = node(1, None)
        Adj[1] = node(2, None)
        
        self._capture_delete(Adj, 3)
        
        for i in range(3):
            self.assertIsNone(Adj[i])
    
    def _capture_delete(self, adj, nodenum):
        captured = io.StringIO()
        sys.stdout = captured
        deleteGraph(adj, nodenum)
        sys.stdout = sys.__stdout__


if __name__ == "__main__":
    unittest.main()
