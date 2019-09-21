"""main"""
def main():
    """main docx"""
    money = float(input())
    lim = float(input())
    promo = float(input()) / 100
    more = float(input())
    added = money + more
    if money >= lim:
        paypromo1 = money - (money*promo)
    elif added >= lim:
        paypromo1 = added - (added*promo)
    else:
        paypromo1 = added
    diff = paypromo1 - money
    if more == 0:
        print("Yes")
    elif diff > 0:
        print("No %.3f"%abs(diff))
    elif money >= lim:
        if promo*100 == 0:
            print("No %.3f"%abs(more))
        elif 0 < promo*100 < 100: #case 3
            paypromo2 = added - (added*promo)
            print("No %.3f"%abs(paypromo2 - paypromo1))
        else:
            print("Yes")
    elif diff < 0:
        print("Yes %.3f"%abs(diff))
    else:
        print("Yes")
 
main()
