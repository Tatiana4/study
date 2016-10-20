def clock_angle(time):
    hour = int(time[:2])
    min = int(time[3:])

    min_angle = 6 * min

    if hour < 12:
        hour_angle = hour * 30 + min * 0.5
    else:
        hour_angle = (hour - 12) * 30 + min * 0.5

    angle = abs(hour_angle - min_angle)

    if angle > 180:
        angle = 360 - angle
    else:
        angle = angle

    print(angle)

clock_angle('13:42')