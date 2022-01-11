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
                return unravel_dict(child_parent, end)
            return None

    def unravel_dict(self, d: Dict, start: str) -> List:
        """
        Unravel dict for bfs path finding.
        unravel_dict({'a': None, 'b': 'a', 'c': 'b'}, "c") -> [a, b, c]

        :param d: Dictionary mapping each node to its parent.
        :param start: Key in `d` to start unravelling from.
        :return: "Unravled" dict.
        """
        unravelled = [start]
        curr = start

        while curr:
            unravelled.append(d[curr])
            curr = d[curr]

        unravelled.pop(len(unravelled) - 1) # remove the `None` object
        return unravelled[::-1] # reverse so we start at root and end at `end`






