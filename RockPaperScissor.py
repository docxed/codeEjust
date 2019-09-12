"""main"""
def main():
    """main function"""
    pointa, pointb = 0, 0
    turn = ""
    turna, turnb = "", ""
    raw = input().upper()
    for i in raw:
        if turn == "GO":
            turnb += i
            if turna == "R" and turnb == "S":
                pointa += 1
            if turna == "S" and turnb == "P":
                pointa += 1
            if turna == "P" and turnb == "R":
                pointa += 1
            if turnb == "R" and turna == "S":
                pointb += 1
            if turnb == "S" and turna == "P":
                pointb += 1
            if turnb == "P" and turna == "R":
                pointb += 1
            turn = ""
            turna, turnb = "", ""
        else:
            turna += i
            turn = "GO"
    if pointa == pointb:
        print("DRAW", pointa)
    elif pointa > pointb:
        print("A win %d-%d"%(pointa, pointb))
    else:
        print("B win %d-%d"%(pointb, pointa))
 
main()
