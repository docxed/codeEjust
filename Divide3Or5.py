"""main"""
def main():
    """main funtion"""
    num = int(input())
    point = 0
    for i in range(1, num+1):
        if i % 3 == 0 or i % 5 == 0:
            point += i
    print(point)
 
main()
