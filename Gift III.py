"""main"""
def main(time):
    """main function"""
    high, tmp = 0, 0
    for _ in range(time):
        val = int(input())
        if val > high and val > tmp:
            tmp, high = high, val
        if val < high and val > tmp:
            tmp = val
    print("Exit" if tmp == 0 else tmp)
 
main(int(input()))
