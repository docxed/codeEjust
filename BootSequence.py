"""main"""
def main():
    """main function"""
    num = int(input())
    for i in range(1, num+1):
        if i != num:
            last = "_"
        else:
            last = ""
        print(i, end=last)
    print()
 
main()
