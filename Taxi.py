"""main"""
import math as m
def pro_dis(distance):
    """distance to price"""
    if distance <= 1:
        price = 35
    elif distance <= 12:
        price = 35 + ((distance-1) * 5)
    elif distance <= 20:
        price = 35 + ((12-1) * 5) + ((distance-12) * 5.5)
    elif distance <= 40:
        price = 35 + ((12-1) * 5) + ((20-12) * 5.5) + ((distance-20) * 6)
    elif distance <= 60:
        price = 35 + ((12-1) * 5) + ((20-12) * 5.5) + ((40-20) * 6) + ((distance-40) * 6.5)
    elif distance <= 80:
        price = 35 + ((12-1) * 5) + ((20-12) * 5.5) + ((40-20) * 6) + ((60-40) * 6.5) + ((distance-60) * 7.5)
    elif distance > 80:
        price = 35 + ((12-1) * 5) + ((20-12) * 5.5) + ((40-20) * 6) + ((60-40) * 6.5) + ((80-60) * 7.5) + ((distance-80) * 8.5)
    return price

def pro_time(time):
    """time to price"""
    price = time * 1.5
    return price

def progressing(distance, time):
    """price progressing"""
    price_distance = m.ceil(pro_dis(distance))
    price_time = m.floor(pro_time(time))
    while price_distance % 2 == 0:
        price_distance += 1
    while price_time % 2 != 0:
        price_time -= 1
    prize = price_distance + price_time
    return prize

def main():
    """main docx"""
    distance, time = 0, 0
    while 1:
        raw = input().split()
        if raw[0] == "F":
            break
        elif raw[0] == "K":
            distance += int(raw[1])
        elif raw[0] == "W":
            time += int(raw[1])
            distance += int(raw[2])
    prize = progressing(distance, time)
    print(int(prize))

main()
