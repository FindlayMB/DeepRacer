# MODEL TRIAL 2
# VERSION 1
# 1/21/2023

import math


def reward_function(params):
    #Extracting information into readable variables
    waypoints = params['waypoints']
    closest_waypoints_indices = params['closest_waypoints']
    car_heading = params['heading']
    
    next_waypoint = waypoints[closest_waypoints_indices[1]]
    prev_waypoint = waypoints[closest_waypoints_indices[0]]

    #Direction calc
    track_direction = math.atan2(next_waypoint[1] - prev_waypoint[1], next_waypoint[0] - prev_waypoint[0])
    track_direction = math.degrees(track_direction) # Radians to degrees

    direction_diff = abs(track_direction - car_heading)

    # If the difference is greater than 180, we need to substract it from 360
    if direction_diff > 180:
        direction_diff = 360 - direction_diff

    # Using ternary operator to check the direction difference
    reward = 0.5 if direction_diff > 10.0 else 1.0
    return float(reward)