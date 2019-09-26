"""main"""
def main():
    """main"""
    step = int(input())
    level = int(input())
    cnt = 0
    keep = 0
    walk = 0
    while cnt != level:
        stair = int(input())
        if stair > step:
            print("No")
            return
        elif stair + keep >= step:
            walk += 1
            keep -= step
            keep = max(keep, 0)
        elif stair < step:
            keep += stair
        cnt += 1
    print(max(walk, 1))

main()
