import numpy as np
import math
import time
from node import Node, Connection
from Robot import movement, sensing
from sense_hat import SenseHat, ACTION_PRESSED, ACTION_HELD, ACTION_RELEASED




# set target vector and start node
target = np.array([5,5]) # will be provided as input later
current_node = Node()
current_node.evaluate(target)
node_list = []
node_list.append(current_node)

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

sense.get_orientation()
sense.get_compass()


def evaluate_path():
    path = []
    path.append(current_node)

    no_path = True
    searches = 0

    while no_path:
        searches += 1
        check_node = Node()
        # first, search for best connected node
        # then, check against previous node branches
        # finally, select most promising node

        if (check_node.is_target()):
            no_path = False

    else:
        print("route found in %s steps" %searches)

def search_node(node):
    connections = node.get_connections()

    best_score = 1000
    best_node = Node()
    for connection in connections():
        if (connection.get_node().get_score() < best_score):
            best_score = connection.get_node().get_score()
            best_node = connection.get_node()
    
    return best_node
        
def explore_node(node):
    # add movement routine to spin on the spot,
    # stopping in increments to scan
    for i in range(12):
        move.turn_left()
        distance = sensing.get_distance()
        #calculate orientation

        #generate a vector
        vector = np.array([distance])

        new_node = Node()
        node.add_connection(node, vector)
        new_node.evaluate(target)

def move_to_node(tar_node):
    tar_vector = tar_node.get_vector()
    cur_vector = current_node.get_vector()
    route_vector = tar_vector - cur_vector

    # transform vector to bearing
    # turn to face node
    # move forwards to node
    
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

def calibrate_movement():
    # use the proximity sensor to calculate how much
    # ground is covered in a second in all directions

    # this allows for better inertial calculations

    f_speed, b_speed = 0

    dist_before = sensing.get_distance()
    move.move_forward(1)
    dist_after = sensing.get_distance()

    f_speed = (dist_before - dist_after)

    dist_before = sensing.get_distance()
    move.move_backward()
    dist_after = sensing.get_distance()

    b_speed = (dist_after - dist_before)

    return f_speed, b_speed

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

