"""main"""
def main():
    """main"""
    txt = input()
    alpha = [i for i in txt if i.isalpha()]
    tmp, digit, get, keep = [], [], "", ""
    for i in txt:
        if not i.isdigit():
            tmp.append(get)
            get = ""
        get += i
    for i in tmp:
        for j in i:
            if j.isdigit():
                keep += j
        digit.append(keep)
        keep = ""
    print(*list(map(lambda txt, num: txt * int(num), alpha, digit)), sep="")
 
main()
