"""main"""
def main():
    """main"""
    num = int(input())
    lst = []
    check = ""
    for i in range(2, num+1):
        for j in range(2, i):
            if i % j == 0:
                check = "No"
        if check != "No":
            lst.append(i)
        check = ""
    print(len(lst))
 
main()
