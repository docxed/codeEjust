"""main"""
def main():
    """main"""
    num = [abs(int(input())) for _ in range(10)]
    num = list(map(str, num))
    for i in range(len(num)):
        if len(num[i]) < 2:
            first = int(num[i])
            defirst = 0
            if int(num[i]) % first + defirst == 0:
                print("Yes")
            else:
                print("No")
        else:
            first = int(num[i][0])
            defirst = int(num[i][1])
            if int(num[i]) % first + defirst == 0:
                print("Yes")
            else:
                print("No")

main()
