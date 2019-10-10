"""main"""
def main():
    """main docx"""
    txt = input().lower()
    txt = [i for i in txt]
    res = ""
    last = []
    for i in range(len(txt)):
        if txt[i].isdigit():
            res += txt[i]
        else:
            last.append(res)
            res = ""
    last.append(res)
    last = list(map(int, list(filter(lambda num: num.isdigit(), last))))
    print(sum(last))
 
main()
