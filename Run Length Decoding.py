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
    digit = list(map(int, digit))
    endgame(alpha, digit)
 
def endgame(alpha, digit):
    """end_game function"""
    res = ""
    while 1:
        if alpha == [] and digit == []:
            break
        res += alpha[0] * digit[0]
        alpha.pop(0)
        digit.pop(0)
    print(res)
 
main()
