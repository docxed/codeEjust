"""main"""
def main():
    """main docx"""
    box = float(input())
    weight = sorted(list(map(float, input().split(" "))))
    keep = float()
    slide, cnt = 0, 0
    while keep < box:
        if slide >= len(weight):
            break
        keep += weight[slide]
        slide += 1
        cnt += 1
    if keep > box:
        cnt -= 1
    print(cnt)
 
main()
