import re


class Node:
    #class for defining nodes in the abstract vector map

    def __init__(self, explored = False, los = True, vector = (0,0)):
        #set bools for easy checking of whether node has been physically
        #explored and if there is *potentially* line of sight to the target
        self.explored = explored
        self.los = los

        #prepare variable for storing overall vector
        self.vector = vector

        #set lists for storing the local map as well as the connected nodes
        self.scan = []
        self.connections = []

    def isLoS(self):
        return self.los

    def isExplored(self):
        return self.explored

    def get_vector(self):
        return self.vector

    def add_connection(self, node, vector):
        #function to add connected nodes
        connection = Connection(node, vector)
        self.connections.append(connection)

    def evaluate_vector(self, target):
        if (self.connections.count > 0):
            connection = self.connections[0]
            self.vector = connection.get_node().get_vector() + connection.get_vector()


class Connection:

    def __init__(self, node, vector):
        self.node = node
        self.vector = vector

    def get_node(self):
        return self.node

    def get_vector(self):
        return self.vector
