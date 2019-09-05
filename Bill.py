"""main"""
def main():
    """main funtion"""
    num = int(input())
    if num * (10/100) <= 50:
        num += 50
        num += num * (7/100)
    elif num * (10/100) > 1000:
        num += 1000
        num += num * (7/100)
    else:
        num += num * (10/100)
        num += num * (7/100)
    print("%.2f"%num)
 
main()
