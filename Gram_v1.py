"""main"""
def main():
    """main docx"""
    raw = input()
    txt = [i for i in raw]
    gram, quan = [], []
    cnt = 0
    for i in range(len(txt)):
        if i > 0:
            gram.append(txt[i-1] + txt[i])
    for i in gram:
        for j in range(len(raw)):
            if j > 0:
                if raw[j-1] + raw[j] == i:
                    cnt += 1
        quan.append(cnt)
        cnt = 0
    print(gram[quan.index(max(quan))])
    print(max(quan))
 
main()
