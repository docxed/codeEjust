"""main"""
def main():
    """main function"""
    pad = abs(int(input()))
    side = input()
    txt = input()
    if side.lower() == "left":
        print(txt.ljust(pad))
    elif side.lower() == "center":
        if (pad-len(txt)) % 2 != 0:
            lwak = (pad - len(txt))//2 + 1
            rwak = (pad - len(txt))//2
        else:
            lwak = (pad - len(txt))//2
            rwak = (pad - len(txt))//2
        print(" "*lwak + txt + " "*rwak)
    elif side.lower() == "right":
        print(txt.rjust(pad))
 
main()
