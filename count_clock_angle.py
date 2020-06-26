'''
На вход подается время в формате ЧЧ:ММ в виде строки.
Нужно посчитать угол между минутной и часовой стрелками.
'''

def process_time(time):
    hour, minute = [int(i) for i in time.split(":")]
    if hour > 12:
        hour -= 12
    return hour, minute

def get_angle(hour, minute):
    minute_hand_angle = 360 - (360 / 60 * minute)
    hour_hand_angle = 360 - (360 / 12 * hour + 30 / 60 * minute)
    angle = (max(hour_hand_angle, minute_hand_angle) -
             min(hour_hand_angle, minute_hand_angle))
    return angle if angle < 360 else 0

if __name__ == "__main__":
    time = input("Input time: ")
    hour, minute = process_time(time)
    angle = get_angle(hour, minute)
    print(angle)
