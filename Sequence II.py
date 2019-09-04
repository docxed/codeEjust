"""main"""
def main():
    """main function"""
    num = int(input())
    ber = 0
    for i in range(1, num+num, 2):
        ber += i
        print(ber, end=" ")
    print()
 
main()
