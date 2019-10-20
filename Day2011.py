"""main"""
def main():
    """main docxed"""
    month = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    day, mon = int(input()), int(input())
    counted = day
    for i in range(1, mon):
        counted += month[i]
    date = ["Friday", "Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday"]
    print(date[counted%7])
 
main()
