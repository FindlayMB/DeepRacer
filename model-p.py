def reward_function(params):
    
    #Follow the center line

    distance_from_center = params['distance_from_center']
    track_width = params['track_width']
    all_wheels_on_track = params['all_wheels_on_track']
    car_speed = params['speed']

    # 5 Markers on Track / EXPANDED VERSION

    mark_1 = 0.1 * track_width
    mark_2 = 0.20 * track_width
    mark_3 = 0.30 * track_width
    mark_4 = 0.40 * track_width
    mark_5 = 0.5 * track_width

    # The more center the car, the more rewards it gets

    if distance_from_center <= mark_1 and all_wheels_on_track:
        reward = 5

    elif distance_from_center <= mark_2 and all_wheels_on_track:
        reward = 4.5

    elif distance_from_center <= mark_3 and all_wheels_on_track:
        reward = 3.5

    elif distance_from_center <= mark_4 and all_wheels_on_track:
        reward = 3

    elif distance_from_center <= mark_5 and all_wheels_on_track:
        reward = 2.5

    else:
        reward = 1e-3

    if car_speed < 1:
        reward += 4

    else:
        reward += 5

    return float(reward)