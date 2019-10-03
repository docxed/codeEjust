"""main"""
def main():
    """main"""
    height = int(input())
    level = int(input())
    cnt, keep, tmp = 0, 0, 0
    while 1:
        if cnt == level:
            break
        val = int(input())
        if val > height:
            print("NO")
            return
        elif tmp > 0 or val < height:
            if val == height:
                keep += 1
                tmp = 0
            elif tmp + val > height:
                keep += 1
                tmp -= tmp
            tmp += val
            if tmp >= height:
                keep += 1
                tmp -= height
        elif val == height:
            if val != 0:
                keep += 1
        cnt += 1
    if tmp > 0:
        keep += 1
    print(keep)
 
main()
