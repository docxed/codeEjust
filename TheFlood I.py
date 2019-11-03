"""main"""
def main():
    """main docx"""
    sand = list(map(int, input().split()))
    time = 0
    turn = True
    while 0 not in sand:
        sand.sort()
        keep = min(sand)
        if turn == True:
            near = abs(keep - sand[1])
            sand = list(map(lambda x: x - near, sand)) # boost วันที่เท่ากับผลต่าง ทั้ง 2 ค่า
            time += near
            turn = False
            sand[0] = keep
        else:
            sand = list(map(lambda x: x - 1, sand))
            sand[0] = keep
            time += 1
    print(time)

main()
