"""main"""
def main(hour, minn):
    """main function"""
    num1 = minn*6
    num2 = hour*30 + minn*0.5
    if num2-num1 < 6 and num2-num1 >= 0:
        print("True")
    else:
        print("False")

main(int(input()), int(input()))
