"""main"""
def main():
    """main docx"""
    digita, digitb = int(input()), int(input())
    while digitb > 0:
        digita, digitb = digitb, digita % digitb
    print(digita)
 
main()
