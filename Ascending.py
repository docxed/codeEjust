"""main"""
def slide(num):
    """slide sording"""
    for i in range(len(num)):
        small = i
        for j in range(i+1, len(num)):
            if num[small] > num[j]:
                small = j
        num[i], num[small] = num[small], num[i]
    return num
 
def main():
    """main"""
    num = [int(input()) for _ in range(5)]
    num = slide(num)
    _ = [print(i) for i in num]
 
main()
