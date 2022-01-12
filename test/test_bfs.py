# write tests for bfs
import pytest
from search import graph

def test_bfs_traversal():
    """
    TODO: Write your unit test for a breadth-first
    traversal here. Create an instance of your Graph class
    using the 'tiny_network.adjlist' file and assert
    that all nodes are being traversed (ie. returns
    the right number of nodes, in the right order, etc.)
    """
    g = graph.Graph("./data/tiny_network.adjlist")

    # this came from running BFS on the graph in `networkx`, this is my ground truth
    assert g.bfs("Luke Gilbert") == ['Luke Gilbert', '33483487', '31806696', '31626775', '31540829', 'Martin Kampmann',
                                     'Neil Risch', 'Nevan Krogan', '32790644', '29700475', '34272374', '32353859',
                                     '30944313', 'Steven Altschuler', 'Lani Wu', 'Michael Keiser', 'Atul Butte',
                                     'Marina Sirota', 'Hani Goodarzi', '32036252', '32042149', '30727954', '33232663',
                                     '33765435', '33242416', '31395880', '31486345', 'Michael McManus', 'Charles Chiu',
                                     '32025019']
    # this came from running BFS on the graph in `networkx`, this is my ground truth
    assert g.bfs("Marina Sirota") == ['Marina Sirota', '31486345', 'Michael Keiser', '33232663', 'Charles Chiu',
                                      'Martin Kampmann', '33242416', '33483487', '32790644', '31806696', '31626775',
                                      '31540829', 'Atul Butte', 'Luke Gilbert', 'Steven Altschuler', 'Lani Wu',
                                      'Neil Risch', 'Nevan Krogan', '33765435', '31395880', '30944313', '32036252',
                                      '32042149', '30727954', '29700475', '34272374', '32353859', 'Hani Goodarzi',
                                      'Michael McManus', '32025019']

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

    # no path between these two
    assert g.bfs("Luke Gilbert", "Reza Abbasi-Asl") == None

    assert g.bfs("Tony Capra", "34771460") == ['Tony Capra', '32839541', 'Nadav Ahituv', '32728249', 'Yin Shen',
                                               '31956907', 'Franklin Huang', '34771460']

    assert g.bfs("Vasilis Ntranos", "Vasilis Ntranos") == ["Vasilis Ntranos"]

    with pytest.raises(ValueError):
        g.bfs("Luke Gilvert", "Katie Pollard")

