"""Ejudge"""
def main():
    """Main"""
    num = input().split(',')
    num = list(map(int, num))
    happy = 0
    for i in range(len(num)):
        if num[i] >= 80:
            happy += 1
        elif i > 0 and num[i] - num[i-1] >= 10 and num[i] >= 20:
            happy += 1
        else:
            pass
    print(happy)
 
main()
