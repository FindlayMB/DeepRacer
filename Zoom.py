#Created on October 16th
#Creator: Dawson van Vlaanderen
#Current version: 08

import math
def reward_function(params):    
    # Read input parameters
    speed = params['speed']
    go_towards = params['heading'] + params['steering_angle']
    close_waypoint = params['closest_waypoints']
    waypoint_list = params['waypoints']
    distance_from_center = params['distance_from_center']
    track_width = params['track_width']
    wp1 = waypoint_list[close_waypoint[0]]
    wp2 = waypoint_list[close_waypoint[1]]
    
    #Finds the angle of a line connecting the next two waypoints in relation to x axis, going from -180 to 180
    #First two if statements that have x==0 are required to avoid dividing by zero
    next_wp_angle = math.degrees(math.atan2(wp2[1] - wp1[1],wp2[0] - wp1[0]))

    #change reward based off of angle compared to next two waypoints
    #find the difference between the current angle + angle of wheels and the angle of waypoints
    diff = abs(next_wp_angle - go_towards)
    if diff > 180:
        diff = 360 - diff

    # checks to see if it is close to the left border, gives reward accordingly
    if (0 <= distance_from_center <= 0.2):
        reward = 10
    elif (0.2 <= distance_from_center <= 0.5):
        reward = 8
    elif (0.5 <= distance_from_center <= (track_width / 2)):
        reward = 5
    else: reward = 1e-3

    #changes reward based off of difference
    if 0 <= diff < 5:
        reward *=2.2
    elif 5 <= diff < 10:
        reward *=2
    elif 10 <= diff < 15:
        reward *=1.5

    #rewards model based of of how fast it is
    reward *= (speed*2)

    # Always return a float value
    return float(reward)
