"""main"""
def main():
    """main docx"""
    num = int(input())
    res = "YES"
    if num == 1:
        return print("NO")
    for i in range(2, int(num**.5) + 1):
        if num % i == 0:
            res = "NO"
            break
    print(res)
 
main()
