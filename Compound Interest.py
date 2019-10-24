"""main"""
def main():
    """main docx"""
    money = float(input())
    rate = float(input())/100
    year = int(input())
    for _ in range(year):
        money += money*rate
    print("%.2f"%money)

main()
