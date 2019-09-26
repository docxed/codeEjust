"""main"""
def main():
    """main"""
    num = int(input())
    for i in range(num):
        if i == 0 or i == num-1:
            print(
                "*" + " "*(num-2) + "*"
            )
        else:
            print(
                "*" + " "*(i-1) + "*" + " "*(num-i-2) + "*"
            )

main()
