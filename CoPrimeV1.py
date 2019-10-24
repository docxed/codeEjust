"""main"""
def main():
    """main docx"""
    digita, digitb = int(input()), int(input())
    while digitb > 0:
        digita, digitb = digitb, digita % digitb
    if digita == 1:
        print("YES")
    else:
        print("NO")
    print(digita)
 
main()
