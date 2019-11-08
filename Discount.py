"""main"""
def main():
    """main docx"""
    books = []
    while 1:
        book = input()
        if book == "ENTER":
            break
        books.append(int(book))
    price = sum(books)
    cnt, get = len(books), 0
    if cnt <= 5:
        get = 0
    elif cnt < 12:
        get = 1
    elif cnt < 20:
        get = 2
    elif cnt < 25:
        get = 4
    else:
        get = cnt // 5
    books = sorted(books)
    for i in range(get):
        price -= books[i]
    print(price)

main()
