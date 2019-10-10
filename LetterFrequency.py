"""main"""
def main():
    """main docx"""
    txt = input().lower()
    txt = [i for i in txt if i.isalpha()]
    diff = sorted(list(set(txt)))
    num = []
    for i in range(len(diff)):
        num.append(txt.count(diff[i]))
    print(diff[num.index(max(num))])

main()
