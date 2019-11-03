"""main"""
def radius(axised):
    """radius"""
    return abs(axised[0]**2 + axised[1]**2)**.5

def main():
    """main docx"""
    axis = [list(map(int, input().split())) for _ in range(int(input()))]
    score = 0
    for i in axis:
        if 0 <= radius(i) <= 2:
            score += 5
        elif 2 < radius(i) <= 4:
            score += 4
        elif 4 < radius(i) <= 6:
            score += 3
        elif 6 < radius(i) <= 8:
            score += 2
        elif 8 < radius(i) <= 10:
            score += 1
    print(score)

main()
