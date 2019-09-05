"""main"""
def main():
    """main function"""
    prize = int(input())
    buy = int(input())
    getfree = int(input())
    want = int(input())
    buyget = buy + getfree
    pay1 = (want//buyget)*((prize*buy))+(want%buyget)*prize
    pay2 = ((want//buyget)+1)*(prize*buy)
    if pay1 >= pay2:
        print(pay2, buyget*((want//buyget)+1))
    else:
        print(pay1, want)

main()
