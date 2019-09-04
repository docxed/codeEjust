"""main"""
def main():
    """main function"""
    num = int(input())
    for i in range(0, num**2, num):
        for j in range(1, num+1):
            print(j+i, end=" ")
        print()
 
main()
