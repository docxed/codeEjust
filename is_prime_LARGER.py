"""main"""
def main():
    """main docx"""
    num = int(input())
    res = "True"
    if num == 1 or num == 0:
        return print("False")
    for i in range(3, int(num**.5) + 1, 2):
        if num % i == 0:
            res = "False"
            break
    print(res)

main()
