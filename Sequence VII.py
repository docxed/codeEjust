"""main"""
def main():
    """main function"""
    num = int(input())
    num2 = num - 1
    for i in range(1, num+1):
        for j in range(1, i+1):
            print(j, end=" ")
        print()
    for i in range(num2, 0, -1):
        for j in range(1, i+1):
            print(j, end=" ")
        print()
 
main()
