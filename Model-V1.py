# MODEL TRIAL 1
# Total lap time
# 
#
# VERSION 1
# 1/22/2023

def reward_function(params):
    # Assign variables from input parameters
    distance_from_center = params['distance_from_center']
    track_width = params['track_width']
    all_wheels_on_track = params['all_wheels_on_track']
    car_speed = params['speed']

    # Set markers for different sections of the track
    center_mark = 0.1 * track_width
    close_to_center_mark = 0.2 * track_width
    middle_mark = 0.3 * track_width
    close_to_edge_mark = 0.4 * track_width
    edge_mark = 0.5 * track_width

    # Check if car is within certain distance from center and all wheels are on track
    if distance_from_center <= center_mark and all_wheels_on_track:
        reward = 3

    elif distance_from_center <= close_to_center_mark and all_wheels_on_track:
        reward = 2.5

    elif distance_from_center <= middle_mark and all_wheels_on_track:
        reward = 1.5

    elif distance_from_center <= close_to_edge_mark and all_wheels_on_track:
        reward = 1

    elif distance_from_center <= edge_mark and all_wheels_on_track:
        reward = 0.5

    else:
        reward = 1e-3

    # Check car speed and add bonus reward
    if car_speed < 0.85:
        reward += 0.5
    else:
        reward += 1.0

    return float(reward)

