"""main"""
def main():
    """main function"""
    lst = []
    new = ""
    raw = input()
    for i in raw:
        lst.append(int(i))
    method_1 = sum(lst)
    method_2 = int("%d%d%d"%(lst[-3], lst[-2], lst[-1])) * 10
    key = method_1 + method_2
    key = str(key)
    if len(key) > 4:
        for i in range(1, 4+1):
            new += str(key[-i])
        print(new[::-1])
    elif int(key) < 1000:
        key = int(key) + 1000
        print(key)
    else:
        print(key)
 
main()
