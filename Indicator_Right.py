"""main"""
def main():
    """main funtion"""
    star, height = int(input()), int(input())
    for i in range(height//2):
        print(" "*(i) + "*"*star)
    for j in range(1, height//2+1+1):
        print(" "*((height//2+1)-j) + "*"*star)
 
main()
