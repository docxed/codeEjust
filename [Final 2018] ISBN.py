"""main"""
def converting(num):
    """convert str to int"""
    if num.isdigit():
        return int(num)
    else:
        return 10
 
def product(fore, back):
    """product of number"""
    return fore * back
 
def main():
    """main docx"""
    isbn = list(map(converting, [i for i in "".join(input().split("-"))]))
    pos = 0
    product_of_number = list()
    for i in range(10, 1, -1):
        result = product(i, isbn[pos])
        product_of_number.append(result)
        pos += 1
    sum_of_product = -(sum(product_of_number))
    modu = sum_of_product % 11
    if modu == isbn[-1]:
        print("Yes")
    else:
        modu = "X" if modu == 10 else modu
        print("No", modu)
 
main()