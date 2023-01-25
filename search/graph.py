import sys
import networkx as nx
import pathlib
import matplotlib
import scipy

#creating graph class
class Graph:
    def __init__(self, filename: str):
        self.filename = filename
        self.store = True

#creating instance of graph class
        self.graph = nx.read_adjlist(filename, delimiter=";", create_using=nx.DiGraph)
    
#main bfs function: AKA "clunky boi" 
def bfs(graph, source_node, end_node=None):
        #creating empty list objects for queue visited nodes and traversal path
    queue=[]
    visited=[]
    traversal=[]
    if end_node == None:
        visited.append(source_node)
        queue.append(source_node)
        #creating loop for visiting each node
        while queue:
            current_node= queue.pop(0)
            traversal.append(current_node)
            print(current_node, end=" ")
        #checking all neighbor nodes of current node
            for neighbor in graph[current_node]:
                if neighbor not in visited :
                    visited.append(neighbor)
                    queue.append(neighbor)
        return(graph)
        ###implementing shortest path search if  end node is provided
    if end_node != None:
        #initializing new list of visited nodes for shortest path implementation
        visitedSP = []
        queue = [[source_node]]
        #checking possible edge case where source_node= end_node
        if source_node == end_node:
            print("Same Node")
            return
        # Loop to traverse the graph with the help of the queue
        while queue:
            path = queue.pop(0)
            node = path[-1]
        # Condition to check whether or not node is in visitedSP
            if node not in visitedSP:
                neighbours = graph[node]
        # Loop to iterate over the neighbours of the node
                for neighbour in neighbours:
                    new_path = list(path)
                    new_path.append(neighbour)
                    queue.append(new_path)
        # Condition to check if the neighbour node is the goal
                    if neighbour == end_node:
                        print(new_path)
                        return new_path
                visitedSP.append(node)
        #conditon to cehck if no path to the end_node exists
        print("connecting path does not exist")
        return