"""main"""
def main():
    """main funtion"""
    even, odd = 0, 0
    while 1:
        num = int(input())
        if num == 0:
            break
        if num % 2 == 0:
            even += num
        elif num % 2 != 0:
            odd += num
    if even == odd:
        print("Draw", odd)
    elif even > odd:
        print("Even", even)
    else:
        print("Odd", odd)
 
main()
