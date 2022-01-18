# write tests for bfs
import pytest
from search import graph
import networkx as nx

def test_bfs_traversal():
    """
    TODO: Write your unit test for a breadth-first
    traversal here. Create an instance of your Graph class
    using the 'tiny_network.adjlist' file and assert
    that all nodes are being traversed (ie. returns
    the right number of nodes, in the right order, etc.)
    """
    g = graph.Graph("./data/tiny_network.adjlist")
    g_nx = nx.read_adjlist("./data/tiny_network.adjlist", create_using=nx.DiGraph, delimiter=";")

    # running BFS on the graph in `networkx`, this is my ground truth -- run this on all nodes and assert output is the
    # same
    for node in g.graph.nodes():
        assert g.bfs(node) == [n for n in nx.bfs_tree(g_nx, node)]

    # test a node that isn't in the graph
    with pytest.raises(ValueError):
        g.bfs("Martin Kampman")

def test_bfs():
    """
    TODO: Write your unit test for your breadth-first
    search here. You should generate an instance of a Graph
    class using the 'citation_network.adjlist' file
    and assert that nodes that are connected return
    a (shortest) path between them.

    Include an additional test for nodes that are not connected
    which should return None.
    """
    g = graph.Graph("./data/citation_network.adjlist")
    g_nx = nx.read_adjlist("./data/citation_network.adjlist", create_using=nx.DiGraph, delimiter=";")

    # no path between these two
    assert g.bfs("Luke Gilbert", "Reza Abbasi-Asl") == None

    assert g.bfs("Tony Capra", "34771460") == ['Tony Capra', '32839541', 'Nadav Ahituv', '32728249', 'Yin Shen',
                                               '31956907', 'Franklin Huang', '34771460']
    # there is more than one shortest path between these two nodes, but the length of the different shortest paths
    # must be the same 
    assert len(g.bfs("Tony Capra", "34771460")) == len([n for n in nx.shortest_path(g_nx, "Tony Capra", "34771460")])
    assert len(g.bfs("Hani Goodarzi", "Vasilis Ntranos")) == len([n for n in nx.shortest_path(g_nx, "Hani Goodarzi",
                                                                                              "Vasilis Ntranos")])

    assert g.bfs("Vasilis Ntranos", "Vasilis Ntranos") == ["Vasilis Ntranos"]

    with pytest.raises(ValueError):
        g.bfs("Luke Gilvert", "Katie Pollard")

