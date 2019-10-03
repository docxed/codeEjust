"""main"""
def main():
    """main"""
    raw = input()
    raw = raw.split()
    keep, get = "", []
    for i in range(len(raw)):
        for j in raw[i]:
            if j.isalpha():
                keep += j
        get.append(keep)
        keep = ""
    raw.clear()
    for i in range(len(get)):
        if len(get[i]) > 6:
            raw.append(get[i])
    print(*raw, sep=" ")
 
main()
