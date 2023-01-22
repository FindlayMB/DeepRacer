# MODEL TRIAL 3
# Total lap time
# 
#
# VERSION 1
# 1/22/2023

def reward_function(params):
    # assign input params
    distance_from_center = params['distance_from_center']
    track_width = params['track_width']
    all_wheels_on_track = params['all_wheels_on_track']
    speed = params['speed']

    # arrays of markers and rewards
    markers = [0.1, 0.2, 0.3, 0.4, 0.5]
    rewards = [3, 2.5, 1.5, 1, 0.5]

    # default reward
    reward = 1e-3
    # loop through markers and rewards
    for i in range(5):
        # check distance from center and all wheels on track
        if distance_from_center <= markers[i] * track_width and all_wheels_on_track:
            reward = rewards[i]
            break

    # check speed and add bonus
    if speed < 1:
        reward += 0.5
    else:
        reward += 1

    return reward
