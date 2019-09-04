"""main"""
def main():
    """main function"""
    num = int(input())
    cnt = 0
    for j in range(num, 0, -1):
        if cnt == 7:
            print()
            cnt = 0
        print(j, end=" ")
        cnt += 1
    print()
 
main()
