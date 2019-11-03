"""main"""
import math as m
def main():
    """main docx"""
    time = list(map(int, input().split()))
    home = [list(map(int, input().split())) for _ in range(time[1])]
    areas = []
    pie = 3.1416
    for dot in home:
        area = pie * m.hypot(dot[0], dot[1])**2
        areas.append(area)
    _ = [print(m.ceil(i / time[0])) for i in areas]

main()
