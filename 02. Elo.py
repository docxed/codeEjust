"""main"""
def main():
    """main"""
    ratea = float(input())
    rateb = float(input())
    turn = input()
    if turn.lower() == "a":
        rea = (1)/(1 + 10**((rateb-ratea) / 400))
        print("%.2f"%rea)
    else:
        reb = (1)/(1 + 10**((ratea-rateb) / 400))
        print("%.2f"%reb)

main()
