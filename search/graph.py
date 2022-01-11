import networkx as nx
from typing import Dict, List

class Graph:
    """
    Class to contain a graph and your bfs function
    """
    def __init__(self, filename: str):
        """
        Initialization of graph object which serves as a container for 
        methods to load data and

        """
        self.graph = nx.read_adjlist(filename, create_using=nx.DiGraph, delimiter=";")

    def bfs(self, start, end=None):
        """
        TODO: write a method that performs a breadth first traversal and pathfinding on graph G

        * If there's no end node, just return a list with the order of traversal
        * If there is an end node and a path exists, return a list of the shortest path
        * If there is an end node and a path does not exist, return None
        
        """

        visited = [start]
        q = [start]
        child_parent = {start: None}

        while q:
            curr = q.pop(0)

            for out_n in self.graph.neighbors(curr):
                if out_n not in visited:
                    q.append(out_n)
                    visited.append(out_n)
                    if end:
                        child_parent[out_n] = curr

        if not end:
            return visited
        else:

            if end in child_parent:
                return []
            return None

    def unravel_dict(d: Dict) -> List:
        """
        
        """






