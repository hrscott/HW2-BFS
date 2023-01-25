# write tests for bfs
import pytest
import search
import pathlib
import difflib
#import matplotlib
import networkx as nx

#creating objects that represent paths to data
citation_network_dir= pathlib.Path(__file__).resolve().parent / "data/citation_network.adjlist"
tiny_network_dir= pathlib.Path(__file__).resolve().parent / "data/tiny_network.adjlist"

#creating graph objects from above paths
data_full= nx.read_adjlist(citation_network_dir, delimiter=";", create_using=nx.DiGraph)
data_tiny= nx.read_adjlist(tiny_network_dir, delimiter=";", create_using=nx.DiGraph)


### TESTING

#testing to ensure that my bfs function yields a full traversal of the citation_network dataset 

#printing the dimensions of the citation_network dataset (yields 5210 nodes and 9247 edges)
print(data_full)

def test_full_traversal():
  
   data_full= nx.read_adjlist(citation_network_dir, delimiter=";", create_using=nx.DiGraph)
   my_data=list(search.bfs(data_full, source_node="Lani Wu"))

   assert len(my_data)==5210


#testing to ensure that my shortest-path functionality is valid via comparison with the output of networkx's
# bidirectional_shortest_path function
def test_bfs():
#creating example of networkx bidirectional_shortest_path
    test_data1=nx.bidirectional_shortest_path(data_full, source="Lani Wu", target="Marina Sirota")
# recreating the same shortest path given identical start/end nodes with my function
    my_data1=search.bfs(data_full,"Lani Wu","Marina Sirota")

    assert my_data1==test_data1


#providing traversal of mini data set as requested ingrading rubric??
#this test is just intended to show the output traversal
def test_traversal_mini_data():
    my_data2=search.bfs(data_tiny,"Lani Wu")
    pass
