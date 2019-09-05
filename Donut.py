"""main"""
def main():
    """main function"""
    price, buy, get, want = int(input()), int(input()), int(input()), int(input())
    getfree = buy + get
    sale = (want//getfree) * (price*buy) + (want%getfree) * price
    sales = ((want//getfree) + 1) * (price*buy)
    if sale >= sales:
        print(sales, getfree * ((want//getfree) + 1))
    else:
        print(sale, want)
 
main()
