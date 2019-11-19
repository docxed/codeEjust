"""main"""
def main():
    """main docx"""
    price = float(input())
    pro_1 = list(map(float, input().split()))
    pro_2 = list(map(float, input().split()))
    type_1, type_2 = False, False
    if price >= pro_1[1]:
        prize_1 = price - pro_1[0]
    else:
        prize_1 = price
        type_1 = True
    if price >= pro_2[1]:
        prize_2 = price - (price*(pro_2[0]/100))
    else:
        prize_2 = price
        type_2 = True
    if type_1 == True and type_2 == True:
        print("Nope")
    elif prize_1 == prize_2:
        if pro_1[1] <= pro_2[1]:
            print("1 %.1f"%prize_1)
        else:
            print("2 %.1f"%prize_2)
    elif prize_1 < prize_2:
        print("1 %.1f"%prize_1)
    else:
        print("2 %.1f"%prize_2)
 
main()