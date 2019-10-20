"""main"""
def main():
    """main docx"""
    num = int(input())
    cnt = 0
    for i in range(1, num + 1):
        for j in range(2, int(i**.5)+1):
            if i % j**2 == 0:
                cnt -= 1
                break
        cnt += 1
    print(cnt)
 
main()
