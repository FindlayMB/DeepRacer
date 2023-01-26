def reward_function(params):
    # Example of rewarding the agent to follow center line

    # Read input parameters
    track_width = params['track_width']
    distance_from_center = params['distance_from_center']
    heading = params['heading']
    speed = params['speed']
    is_left_of_center = params['is_left_of_center']

    # Calculate 3 markers that are at varying distances away from the center line
    marker_1 = 0.1 * track_width
    marker_2 = 0.25 * track_width
    marker_3 = 0.5 * track_width

    # Give higher reward if the car is closer to center line and vice versa
    if distance_from_center <= marker_1:
        reward = 1.3
    elif distance_from_center <= marker_2:
        reward = 0.4
    elif distance_from_center <= marker_3:
        reward = 0.08
    else:
        reward = 1e-3 # likely crashed/ close to off track
    
    # The following is to dictate how the car will turn
    #if turning left
    if heading < 0:
        if is_left_of_center:
            reward *= 0.7
        else:
            reward *= 1.5
    # if turning right
    elif heading > 0:
        if is_left_of_center:
            reward *= 1.5
        else:
            reward *= 0.7
    
    reward *= speed

    return float(reward)
