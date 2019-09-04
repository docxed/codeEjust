"""main"""
def circle(myx, myy, itx, ity):
    """circle function"""
    return (itx - myx)**2 + (ity - myy)**2
 
def main():
    """main function"""
    myx, myy = float(input()), float(input())
    distance = float(input())
    itx, ity = float(input()), float(input())
    res = (circle(myx, myy, itx, ity))**.5
    if res <= distance:
        print("Yes")
        return
    print("No")
 
main()
