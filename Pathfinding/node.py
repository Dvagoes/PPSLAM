import numpy as np


class Node:
    # class for defining nodes in the abstract vector map

    def __init__(self, explored = False, los = True, vector = np.array([0,0])):
        # set bools for easy checking of whether node has been physically
        # explored and if there is *potentially* line of sight to the target
        self.explored = explored
        self.los = los

        # prepare variable for storing overall vector
        self.vector = vector
        self.score = 0

        # set lists for storing the local map as well as the connected nodes
        self.scan = []
        self.connections = []

    def hasLoS(self):
        return self.los

    def isExplored(self):
        return self.explored

    def get_vector(self):
        return self.vector
    
    def get_score(self):
        return self.score

    def add_connection(self, node, vector):
        # function to add connected nodes
        connection = Connection(node, vector)
        self.connections.append(connection)

    def get_connections(self):
        return self.connections

    def evaluate_vector(self, target):
        # checks if any connected nodes (if not, it is the start node)
        if (self.connections.count > 0):
            connection = self.connections[0]
            self.vector = connection.get_node().get_vector() + connection.get_vector()
            
        self.score = np.linalg.norm(self.vector - target)

    def is_target():
        # helper method to check if target has been reached
        # will add tolerances to account for innacuracies in movement
        return True


class Connection:

    def __init__(self, node, vector):
        self.node = node
        self.vector = vector

    def get_node(self):
        # get the connected node
        return self.node

    def get_vector(self):
        # get vector between nodes
        return self.vector
