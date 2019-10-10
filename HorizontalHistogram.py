"""main"""
def main():
    """main docx"""
    txt = input()
    rawlow = [i for i in txt if i.islower()]
    rawhigh = [i for i in txt if i.isupper()]
    low = sorted(list(set([i for i in txt if i.islower()])))
    high = sorted(list(set([i for i in txt if i.isupper()])))
    for i in low:
        pipe = "-"*rawlow.count(i)
        hyp = ""
        fix = 0
        for j in range(len(pipe)):
            hyp += pipe[j]
            fix += 1
            if fix % 5 == 0 and j+1 != len(pipe):
                hyp += "|"
        print(i, ":", hyp)
    for i in high:
        pipe = "-"*rawhigh.count(i)
        hyp = ""
        fix = 0
        for j in range(len(pipe)):
            hyp += pipe[j]
            fix += 1
            if fix % 5 == 0 and j+1 != len(pipe):
                hyp += "|"
        print(i, ":", hyp)
 
main()
