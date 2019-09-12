"""main"""
def main():
    """main function"""
    txt = input()
    if "A" <= txt[0].upper() <= "Z":
        print("Hello", txt + ".")
    else:
        print("สวัสดี", txt)

main()
