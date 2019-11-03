"""main"""
def istax(money):
    """progress tax"""
    if money <= 150000:
        money = 0
    elif money <= 300000:
        money = (money-150000) * .05
    elif money <= 500000:
        money = (money-300000) * .10 + 7500
    elif money <= 750000:
        money = (money-500000)*.15 + 27500
    elif money <= 1000000:
        money = (money-750000) * .20 + 65000
    elif money <= 2000000:
        money = (money-1000000) * .25 + 115000
    elif money <= 4000000:
        money = (money-2000000) * .30 + 365000
    else:
        money = (money-4000000) * .35 + 965000
    return money


def main():
    """main docx"""
    money = int(input())
    print(int(istax(money)))

main()
