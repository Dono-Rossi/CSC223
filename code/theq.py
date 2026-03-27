import sys


class node:
    def __init__(self, vertex, next):
        self.vertex = vertex
        self.next = next

def createGraph(Adj, nodeNum):
    for i in range(nodeNum):
        last = None 
        n = int(input(f"\n Enter the number of neighbors of {i}: "))
        for j in range(n):
            val = int(input(f" Enter the neighbor {j} of {i}: "))
            nodei = node(val, None)
            if (Adj[i] == None):
                Adj[i] = nodei
            else:
                last.next = nodei
            last = nodei


def displayGraph(Adj, nodeNum):
    """Prints the graph structure to the console (Replacement for maxh __repr__)."""
    print("\n The Graph is: ")
    for i in range(nodeNum):
        print(f" Node {i}: ", end="")
        ptr = Adj[i]
        if ptr is None:
            print("—", end="")
        while ptr is not None:
            print(f"-> {ptr.vertex} ", end="")
            ptr = ptr.next
        print()

def to_mermaid(Adj, nodeNum) -> str:
    """Generates a Mermaid graph definition (From maxh.py)."""
    seen_edges = set()
    lines = ["graph TD"]
    for i in range(nodeNum):
        ptr = Adj[i]
        if ptr is None:
            lines.append(f"    {i}") 
        while ptr is not None:
            # Sort to prevent duplicate lines for undirected visualization
            edge = tuple(sorted((i, ptr.vertex)))
            if edge not in seen_edges:
                lines.append(f"    {i} --- {ptr.vertex}")
                seen_edges.add(edge)
            ptr = ptr.next
    return "\n".join(lines)

def deleteGraph(Adj, nodeNum):
    """Clears the graph memory (From maxh.py)."""
    for i in range(nodeNum):
        Adj[i] = None
    print("\n Graph deleted successfully.")


if __name__ == "__main__":
    Adj = []
    for i in range(10): 
        Adj.append(None)

    nodeNum = int(input("\n Enter the number of nodes in G: "))

    for i in range(nodeNum):
        Adj[i] = None

    createGraph(Adj, nodeNum)
    displayGraph(Adj, nodeNum)

    print("\n--- Mermaid Diagram (Copy into Mermaid Live Editor) ---")
    print(to_mermaid(Adj, nodeNum))

    choice = input("\nDo you want to delete the graph? (y/n): ")
    if choice.lower() == 'y':
        deleteGraph(Adj, nodeNum)
        displayGraph(Adj, nodeNum)
