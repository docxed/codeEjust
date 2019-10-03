"""main"""
def main():
    """main"""
    num = int(input())
    if num == 1:
        print("No")
        return
    for i in range(2, num):
        if num % i == 0:
            print("No")
            return
    print("Yes")
 
main()
