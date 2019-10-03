"""main"""
def main():
    """main"""
    num = [abs(int(input())) for _ in range(10)]
    num = list(map(str, num))
    for i in range(len(num)):
        defirt = 0
        if int(num[i]) == 0:
            print("No")
        elif len(num[i]) == 1:
            print("Yes")
        else:
            for j in num[i]:
                defirt += int(j)
            if int(num[i]) % defirt == 0:
                print("Yes")
            else:
                print("No")
 
main()
