"""main"""
def looping(current, stop, point, low, high):
    """loop function"""
    if current == stop:
        if high - low > 2:
            print("Surprising")
            return
        print("Not surprising")
        return
    if 0 <= point + current/10 <= 10 and 0 <= point - current/10 <= 10:
        low = point - current/10
    looping(current+1, stop, point, low, high)
 
def main():
    """main function"""
    alls, high = float(input()), float(input())
    res = (alls - high) / 2
    if alls - high - high == high:
        print("Not surprising")
        return
    looping(1, 10, res, 0, high)
 
main()
