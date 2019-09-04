"""main"""
def main():
    """main funtion"""
    money = int(float(input()) * 100)
    year = int(input())
    for _ in range(year):
        money += int(money * 381)//10000
    raw = money // 100
    dec = money % 100
    print("%d.%02d"%(raw, dec))
 
main()
