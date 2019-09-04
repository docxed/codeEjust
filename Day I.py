"""main"""
def main():
    """main function"""
    year = int(input())
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        print("Yes")
        return
    print("No")
 
main()
