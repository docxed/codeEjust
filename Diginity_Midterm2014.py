"""main"""
def main():
    """main function"""
    arabic = []
    while True:
        num = input()
        if num == "0":
            break
        for i in num:
            arabic.append(int(i))
        while 1:
            new = sum(arabic)
            new = str(new)
            if len(new) == 1:
                print(new)
                arabic.clear()
                break
            elif len(new) > 1:
                arabic.clear()
                for i in new:
                    arabic.append(int(i))
 
main()
