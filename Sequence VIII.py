"""main"""
def main():
    """main function"""
    num = int(input())
    for i in range(num):
        print("   " * (num-i-1), end="")
        for j in range(1, i+2):
            print("%02d"%j, end=" ")
        print()
 
main()
