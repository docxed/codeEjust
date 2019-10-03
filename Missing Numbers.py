"""main"""
def main():
    """main"""
    num = int(input())
    lst, vanish = [], []
    while 1:
        val = int(input())
        if val == 0:
            break
        lst.append(val)
    for i in range(1, num+1):
        if i not in lst:
            vanish.append(i)
    vanish.sort()
    _ = [print(i) for i in vanish]
 
main()
