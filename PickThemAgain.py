"""main"""
def main():
    """main"""
    num = input().split()
    num = list(map(int, num))
    lst = []
    for i in num:
        if i % 3 == 0 or i % 5 == 0:
            lst.append(i)
    if lst == []:
        print("Nope")
    else:
        print(*lst[::-1], sep="\n")
 
main()
