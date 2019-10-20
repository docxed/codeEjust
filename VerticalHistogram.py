"""main"""
def main():
    """main"""
    txt = input()
    rawlow = [i for i in txt if i.islower()]
    rawhigh = [i for i in txt if i.isupper()]
    low = sorted(list(set([i for i in txt if i.islower()])))
    high = sorted(list(set([i for i in txt if i.isupper()])))
    cnted = []
    raw = rawlow + rawhigh
    char = low + high
    for i in char:
        cnted.append(raw.count(i))
    maxpipe = max(cnted)
    star = ""
    for i in range(max(cnted)):
        for j in cnted:
            if j >= maxpipe:
                star += "*"
            else:
                star += " "
        star = [i for i in star]
        print(
            "%03d"%maxpipe, *star, sep=" "
        )
        maxpipe -= 1
        star = ""
    print("   ", *char, sep=" ")
 
main()
