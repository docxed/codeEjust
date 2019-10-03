"""main"""
def main():
    """main"""
    raw = int(input())
    lst = []
    if raw == 0:
        print(0)
        return
    while raw > 0:
        lst.append(raw % 2)
        raw //= 2
    print(*lst[::-1], sep="")
 
main()
