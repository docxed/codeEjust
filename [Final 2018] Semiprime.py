"""main"""


def semiprime(num):
    """progress semiprime"""
    cnt = 0
    for i in range(2, int(num**.5)+1):
        while num % i == 0:
            num /= i
            cnt += 1
        if cnt >= 2:
            break
    if num > 1:
        cnt += 1
    return True if cnt == 2 else False


def main():
    """main"""
    num = int(input())
    cnt = 0
    for i in range(1, num+1):
        if semiprime(i):
            cnt += 1
    print(cnt)


main()
