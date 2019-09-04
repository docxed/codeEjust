"""main"""
def main():
    """main function"""
    num = int(input())
    for i in range(num):
        for j in range(2, num+2):
            print(j+i, end=" ")
        print()
 
main()
