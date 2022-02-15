from ast import Break
from turtle import distance
import numpy as np
import math
import time
from node import Node, Connection
from Robot import movement, sensing
from sense_hat import SenseHat, ACTION_PRESSED, ACTION_HELD, ACTION_RELEASED

# set target vector and start node
target = Node(vector=np.array([5,5])) # will be provided as input later
current_node = Node()
current_node.evaluate(target)
node_list = []
node_list.append(current_node)
explored_list = []

# set up flag for checking if actively running
active = False

def begin_test(event):
    global active
    if event.action != ACTION_RELEASED:
        if (not active):
            move.move_forward()  # change to starting test run
            active = True
        else:
            move.stop()
            active = False

sense = SenseHat()
move = movement.Move()
event = sense.stick.direction_middle = begin_test

def evaluate_path():
    path = []
    path.append(current_node)
    global node_list
    global explored_list
    global target
    no_path = True
    searches = 0
    
    while (no_path):
        searches += 1

        if (check_los(current_node, target)):
            move_to_node(target)
            no_path = False
            break

        # check for best connected unexplored node
        if (not current_node.isExplored()):
            explore_node(current_node)
            current_node.setExplored()
            explored_list.append(current_node)
        
        best_connected = search_node(current_node)

        # search for best explored node
        best_node = current_node
        best_score = best_node.get_score()
        for node in explored_list:
            if (node.get_score() < best_score):
                best_score = node.get_score()
                best_node = node

        if (best_connected.get_score() >  best_score):
            move_to_node(best_connected)
        else:
            path_to_node(best_node)

def path_to_node(target_node):
    global current_node
    path = search_for_path(current_node, target_node)
    for node in path:
        if (check_los(current_node, target_node)):
            move_to_node(target_node)
            current_node = target_node
            break
        else:
            move_to_node(node)
            current_node = node

def search_for_path(start_node, target_node):
    path_from_start = []
    path_from_target = []

    # finds path from target node back to origin

    previous = target_node.get_previous()
    while (not previous.is_target(node_list[0].get_vector())):
        path_from_target.append(previous)
        previous = previous.get_previous()

    # compares previous nodes to find last common node, then derives path

    previous = start_node.get_previous()
    while (not previous.is_target(node_list[0].get_vector())):
        
        for node in path_from_target:
            if (previous.is_target(node.get_vector())):
                index = path_from_target.index(node)
                path = path_from_start + path_from_target[0::index]
                return path
            else:
                path_from_start.append(previous)
                previous = previous.get_previous()        

def search_node(node):
    connections = node.get_connections()
    # low scores are good, as it indicates lower distance
    best_score = node.get_score()
    best_node = node
    for connection in connections():
        if (not connection.get_node().isExplored()):
            if (connection.get_node().get_score() < best_score):
                best_score = connection.get_node().get_score()
                best_node = connection.get_node()
    return best_node

def check_los(start_node, target_node):
    #check LoS between current node and another node

    move_vector = target_node.get_vector() - start_node.get_vector()
    turn_to(vector_to_bearing(move_vector))
    if (sensing.get_distance() >= vector_to_distance(move_vector)):
        start_node.add_connection(target_node, move_vector)
        target_node.add_connection(start_node, -move_vector)
        return True
    else:
        return False

def explore_node(node):
    # add movement routine to spin on the spot,
    # stopping in increments to scan
    # could at later date use a more focused exploration
    # range to optimise time and space complexity

    for i in range(12):
        bearing =  30 * i
        turn_to(bearing)
        clearance = sensing.get_distance()

        # create nodes along every 10cm of clearance

        distance = 10
        
        while (distance < clearance):
            # generate a vector
            vector = bearing_to_vector(distance, bearing)
            coord = node.get_vector() + vector

            # generate node and connections
            new_node = Node(vector=coord)
            new = True
            for n in node_list:
                if (new_node.is_target(n)):
                    node.add_connection(n, vector)
                    n.add_connection(node, -vector)
                    new = False
                    break
            if (new):
                node.add_connection(new_node, vector)
                new_node.add_connection(node, -vector)
                new_node.evaluate(target)
                node_list.append(new_node)
            
            distance += 10
            

def move_to_node(target_node):
    move_vector = target_node.get_vector() - current_node.get_vector()
    turn_to(vector_to_bearing(move_vector))
    move_to(vector_to_distance(move_vector))

    print("moving along vector " + move_vector + " to reach " + target_node.get_vector())
    
def bearing_to_vector(distance, bearing):
    x = distance * np.sin(bearing)
    y = distance * np.cos(bearing)
    return np.array([x, y])

def vector_to_bearing(vector):
    x = vector[0]
    y = vector[1]
    return np.arctan((x/y))

def vector_to_distance(vector):
    x = vector[0]
    y = vector[1]
    return np.sqrt(np.square(x) + np.square(y))

def move_to(distance):
    current_distance = sensing.get_distance()
    target_distance = current_distance - distance

    if (target_distance < 0):
        move.move_backward()
    else:
        move.move_forward()
    
    while (not math.isclose(current_distance, target_distance, abs_tol=1e-3)):
        current_distance = sensing.get_distance()
    else:
        move.stop()

def turn_to(bearing):
    current_bearing = sense.get_compass()

    if (bearing > current_bearing):
        move.turn_right()
    else:
        move.turn_left()
    
    while (not math.isclose(current_bearing, bearing, abs_tol=1e-3)):
        current_bearing = sense.get_compass()
    else:
        move.stop()
    