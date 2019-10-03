"""main"""
def main():
    """main"""
    num = input().split()
    new, tmp, last = [], "", []
    for i in range(len(num)):
        for j in num[i]:
            if j.isdigit():
                tmp += j
        new.append(tmp)
        tmp = ""
    new = list(map(int, new))
    for k in new:
        if k % 2 == 0:
            last.append(k)
    if last == []:
        print("Nope")
        return
    _ = [print(h) for h in last]
 
main()
