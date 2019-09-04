"""main"""
def main():
    """main function"""
    num = int(input())
    for i in range(-(num-1), num):
        for j in range(-(num-1), num):
            print("%02d"%(num-max(abs(i), abs(j))), end=" ")
        print()
 
main()
