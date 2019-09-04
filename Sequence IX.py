"""main"""
def main():
    """main function"""
    num = int(input())
    for i in range(num):
        print(" " * ((num-i-1)*3), end="")
        for j in range(i+1):
            print("%02d"%(j+1), end=" ")
        for k in range(i):
            print("%02d"%(i-k), end=" ")
        print()
 
main()
