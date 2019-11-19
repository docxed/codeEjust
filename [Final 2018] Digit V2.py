"""main"""
def numdict(num):
    """lenght of number"""
    if "thousand" in num:
        lenght = 4
    elif "hundred" in num:
        lenght = 3
    elif "teen" in num or "ty" in num or "twelve" in num or "eleven" in num or "ten" in num:
        lenght = 2
    else:
        lenght = 1
    return lenght
 
def main():
    """main docx"""
    text = input().split()
    list_of_numbers = list()
    for i in text:
        real_num = numdict(i)
        list_of_numbers.append(real_num)
    print(max(list_of_numbers))
 
main()