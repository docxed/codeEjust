"""main"""
def main():
    """main docx"""
    time = int(input())
    time2 = int(input())
    lsta = [int(input()) for _ in range(time)]
    lstb = [int(input()) for _ in range(time2)]
    res = []
    for i in lsta:
        if i not in lstb:
            res.append(i)
    print(*sorted(res), sep=" ")
 
main()
