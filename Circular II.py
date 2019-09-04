"""main"""
def main():
    """main function"""
    myx, myy = float(input()), float(input())
    myd = float(input())
    itx, ity = float(input()), float(input())
    itd = float(input())
    cir = ((myx - itx)**2 + (myy - ity)**2)**.5
    rad = (myd + itd)
    if cir == rad or cir > rad:
        print("No")
    else:
        print("Yes")
 
main()
