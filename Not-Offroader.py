#Created on October 16th
#Creator: Dawson van Vlaanderen
#Current version: 03

import math
def reward_function(params):
    # Example of rewarding the agent to stay inside the two borders of the track
    
    # Read input parameters
    speed = params['speed']
    heading = params['heading']
    steering_angle = params['steering_angle']
    close_waypoint = params['closest_waypoints']
    waypoint_list = params['waypoints']
    distance_from_center = params['distance_from_center']
    track_width = params['track_width']
    distance_from_side = ((track_width / 2) - distance_from_center)/track_width
    wp1 = waypoint_list[close_waypoint[0]]
    wp2 = waypoint_list[close_waypoint[1]]
    x = wp2[0] - wp1[0]
    y = wp2[1] - wp1[1]
    
    #Finds the angle of a line connecting the next two waypoints in relation to x axis, going from -180 to 180
    if x==0 and y>0:
        next_wp_angle = 90
    elif x==0 and y<0:
        next_wp_angle = -90
    else:
        next_wp_angle = math.degrees(math.atan(y / x))
    if x<0 and y>=0:
        next_wp_angle += 180
    elif x<0 and y<=0:
        next_wp_angle += -180
    
    # checks to see if it is close to the left border, gives reward accordingly
    if (0 <= distance_from_side <= 0.2) and (params['is_left_of_center']):
        reward = 0.7
    elif (0.2 <= distance_from_side <= 0.5) and (params['is_left_of_center']):
        reward = 1
    elif (0 <= distance_from_side <= 0.5) and not(params['is_left_of_center']):
        reward = 0.5
    else: reward = 1e-3

    #change reward based off of angle compared to next two waypoints
    #find the difference between the current angle + angle of wheels and the angle of waypoints
    go_towards = steering_angle + heading
    if (go_towards > 0 and next_wp_angle < 0) or (go_towards < 0 and next_wp_angle > 0):
        find_diff1 = 360 - (abs(go_towards) + abs(next_wp_angle))
        find_diff2 = (abs(go_towards) + abs(next_wp_angle))
        if find_diff1 > find_diff2:
            diff = find_diff2
        else: diff = find_diff1
    else: 
        diff = abs(next_wp_angle - go_towards)

    #changes reward based off of difference
    if 0 <= diff <= 5:
        reward *=2.5
        #adjusts reward based off of speed as well
        if speed < 0.7:
            reward *= 0.5
        elif speed < 0.8:
            reward *= 0.7           
        elif speed < 1:
            reward *= 0.9
        else: reward *= 1
    elif 5 <= diff <= 10:
        reward *=2
        if speed < 0.7:
            reward *= 0.4
        elif speed < 0.8:
            reward *= 0.6           
        elif speed < 1:
            reward *= 0.8
        else: reward *= 0.9
    elif 10 <= diff <= 15:
        reward *=1.5
        if speed < 0.7:
            reward *= 0.3
        elif speed < 0.8:
            reward *= 0.5           
        elif speed < 1:
            reward *= 0.7
        else: reward *= 0.8
    elif diff >= 10:
        reward *= 10/diff
        if speed < 0.7:
            reward *= 0.6


    # Always return a float value
    return float(reward)
