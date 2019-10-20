"""main"""
def main():
    """main docxed"""
    num = [int(input()) for _ in range(int(input()))]
    keep, res = [], []
    if 1 in num:
        print(1)
    elif sum(num) == 0:
        print(0)
        return
    turn = True
    for i in range(2, max(num)+1):
        for j in num:
            if j % i == 0:
                res.append(i)
            elif j % i != 0:
                turn = False
        if turn == True:
            for k in res:
                keep.append(k)
        res.clear()
        turn = True
    print(max(keep))
 
main()
