"""main"""
def main():
    """main"""
    num = input().split()
    new, tmp = [], ""
    for i in range(len(num)):
        for j in num[i]:
            if j.isdigit():
                tmp += j
        new.append(tmp)
        tmp = ""
    new = list(filter(lambda num: int(num) % 2 == 0, new))
    _ = [print(h) for h in new if new != []]
    if new == []:
        print("Nope")
 
main()
