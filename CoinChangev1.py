"""main"""
def main():
    """main docx"""
    money = int(input())
    lst = []
    mon_25 = money//25
    lst.append(mon_25)
    mon_25 = money % 25
    mon_10 = mon_25//10
    lst.append(mon_10)
    mon_10 = mon_25 % 10
    mon_5 = mon_10//5
    lst.append(mon_5)
    mon_5 = mon_10 % 5
    lst.append(mon_5)
    print(sum(lst))
 
main()
