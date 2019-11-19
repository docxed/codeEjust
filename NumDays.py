"""main"""
def main():
    """main docx"""
    days_1 = int(input())
    mon_1 = int(input())
    days_2 = int(input())
    mon_2 = int(input())
    date = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8:31, 9: 30, 10: 31, 11: 30, 12: 31}
    counter = 0
    call_1 = date[mon_1]
    if days_1 > call_1:
        print("Impossible")
        return
    call_2 = date[mon_2]
    if days_2 > call_2:
        print("Impossible")
        return
    if mon_1 < mon_2:
        counter += abs(days_1 - date[mon_1])
        mon_1 += 1
        while True:
            if mon_1 == mon_2:
                counter += days_2
                break
            counter += date[mon_1]
            mon_1 += 1
        print(counter)
    elif mon_1 == mon_2:
        counter += abs(days_1 - days_2)
        print(counter)
    elif mon_1 > mon_2:
        counter += days_2
        mon_1 -= 1
        while True:
            if mon_1 == mon_2:
                counter += abs(date[mon_1] - days_1)
                break
            counter += date[mon_1]
            mon_1 -= 1
        print(counter)
 
main()