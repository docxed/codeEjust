"""main"""
def main():
    """main function"""
    hour, mins = int(input()), int(input())
    if 0 <= (hour*30 + mins*.5) - (mins*6) < 6:
        print("True")
        return
    print("False")

main()
