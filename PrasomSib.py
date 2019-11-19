"""main"""
def main():
    """main docx"""
    raw = [int(i) for i in input()]
    cnt = 0
    while raw != []:
        keep = raw[0]
        raw.pop(0)
        counter = 0
        while keep < 10 and counter != len(raw):
            keep += raw[counter]
            if keep == 10:
                cnt += 1
                break
            counter += 1
    print(cnt)
 
main()