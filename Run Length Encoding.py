"""main"""
def main():
    """main"""
    txt = input()
    lst = []
    turn = txt[0]
    cnt = 0
    for i in txt:
        if i != turn:
            lst.append(cnt)
            lst.append(turn)
            cnt = 0
            turn = i
        if i == turn:
            cnt += 1
        pointnum, pointtxt = cnt, turn
    lst.append(pointnum)
    lst.append(pointtxt)
    lst = list(map(str, lst))
    print("".join(lst))
 
main()
