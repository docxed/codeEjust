"""main"""
def check(num):
    """check prime"""
    if num == 1:
        return 0
    for i in range(2, int(num**.5) + 1):
        if num % i == 0:
            return 0
    return num
 
def circular(num):
    """cir num"""
    num = str(num)
    lst = [int(num)]
    cnt = 0
    while cnt < len(num) - 1:
        num = num[1::] + num[0]
        lst.append(int(num))
        cnt += 1
    return lst
 
def main():
    """main"""
    end = int(input())
    keep = []
    for run in range(1, end + 1):
        if run > 9:
            lstcired = circular(run)
            chk = list(map(check, lstcired))
            if 0 not in chk:
                keep.append(run)
        else:
            keep.append(check(run))
    print(sum(keep))
 
main()
