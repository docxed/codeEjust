"""main"""
def main():
    """main docx"""
    rec1 = list(map(int, input().split()))
    rec2 = list(map(int, input().split()))
    left1 = [rec1[0], rec1[1]]
    left2 = [rec2[0], rec2[1]]
    right1 = [rec1[0]+rec1[2], rec1[1]+rec1[3]]
    right2 = [rec2[0]+rec2[2], rec2[1]+rec2[3]]
    laping = (min(right1[0], right2[0]) - max(left1[0], left2[0])) * (min(right1[1], right2[1]) - max(left1[1], left2[1]))
    print(laping if laping > 0 else "no overlapping")

main()
