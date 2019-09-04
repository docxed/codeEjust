"""main"""
def main():
    """main function"""
    start, time = int(input()), int(input())
    if start == time:
        print(start)
    elif start < time:
        for i in range(start, time + 1):
            print(i)
    elif start > time:
        for i in range(start, time - 1, -1):
            print(i)
 
main()
