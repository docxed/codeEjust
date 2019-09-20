"""main"""
def main():
    """main docx"""
    price = int(input())
    cap = int(input())
    promo = int(input())
    money = int(input())
    milk, bottle = 0, 0
    while money >= price:
        money -= price
        milk += 1
    while milk >= cap:
        if cap == 0:
            break
        milk -= cap
        bottle += cap
        milk += promo
    print(bottle+milk)
 
main()
