value = int(input('Please input your speed: '))

def check_speed(speed):
    points = 0
    if speed < 70:
        return 'Ok'
    else:
        for i in range(75, speed + 1):
            if i % 5 == 0:
                points += 1
        if points > 12:
            return 'License suspended'
        else:
            return points

print(check_speed(value))
