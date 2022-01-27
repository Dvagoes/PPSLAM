import numpy as np
from node import Node
from Robot import movement, sensing


# set target vector and start node
target = (5,5) # will be provided as input later
current_node = Node()
current_node.evaluate_vector(target)
node_list = []
node_list.append(current_node)


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
        movement.turn_left(1)
        distance = sensing.get_distance()
        #calculate orientation

        #generate a vector
        vector = np.array([distance])

        new_node = Node(vector=vector)

def calibrate_movement():
    # use the proximity sensor to calculate how much
    # ground is covered in a second in all directions

    # this allows for better inertial calculations

    f_speed, b_speed = 0

    dist_before = sensing.get_distance()
    movement.move_forward(1)
    dist_after = sensing.get_distance()

    f_speed = (dist_before - dist_after)

    dist_before = sensing.get_distance()
    movement.move_backward(1)
    dist_after = sensing.get_distance()

    b_speed = (dist_after - dist_before)