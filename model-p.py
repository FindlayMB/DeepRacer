def reward_function(params):
    
    distance_from_center = params['distance_from_center']
    track_width = params['track_width']
    all_wheels_on_track = params['all_wheels_on_track']
    car_speed = params['speed']

    # 5 Markers on Track

    marker_1 = 0.1 * track_width
    marker_2 = 0.20 * track_width
    marker_3 = 0.30 * track_width
    marker_4 = 0.40 * track_width
    marker_5 = 0.5 * track_width

    # The more center the car, the more rewards it gets

    if distance_from_center <= marker_1 and all_wheels_on_track:
        reward = 5

    elif distance_from_center <= marker_2 and all_wheels_on_track:
        reward = 4.5

    elif distance_from_center <= marker_3 and all_wheels_on_track:
        reward = 3.5

    elif distance_from_center <= marker_4 and all_wheels_on_track:
        reward = 3

    elif distance_from_center <= marker_5 and all_wheels_on_track:
        reward = 2.5

    else:

        reward = 1e-3  # likely crashed/ close to off track

    if car_speed < 1:
        reward = reward + 2

    else:
        reward = reward + 3

    return float(reward)