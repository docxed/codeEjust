"""main"""
def main():
    """main"""
    numa, numb = abs(int(input())), abs(int(input()))
    lst = []
    if numa == 1 or numb == 1:
        lst.append(1)
    elif numa == 0 and numb == 0:
        print(0)
        return
    for i in range(2, max(numa, numb)+1):
        if numa % i == 0 and numb % i == 0:
            lst.append(i)
    if lst == []:
        lst.append(1)
    print(max(lst))
 
main()
