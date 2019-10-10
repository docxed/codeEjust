"""main"""
def main():
    """main docx"""
    raw = []
    while 1:
        txt = input()
        if txt == "END":
            break
        raw.append(txt)
    raw = sorted(list(map(int, raw)))
    diff = [str(i)[0:4] for i in raw]
    sub = [str(i)[0:4] for i in raw]
    sub = list(map(str, sorted(map(int, (list(set(sub)))))))
    year, subject, human = [], [], []
    for i in range(len(sub)):
        if sub[i][0:2] not in year:
            year.append(sub[i][0:2])
        else:
            year.append("--")
        subject.append(sub[i][2:4])
        human.append(sub[i][0:4])
    for i in range(len(year)):
        print(year[i], int(subject[i]), diff.count(human[i]))
 
main()
