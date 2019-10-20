"""TEST NEW LESSON"""
def fib(num):
    """fibo docx"""
    mata = [[1, 1], [1, 0]]
    if num == 0:
        return 0
    power(mata, num - 1)
    return mata[0][0]
 
def multiply(mata, matb):
    """matrix multiply"""
    posx = (mata[0][0] * matb[0][0] + mata[0][1] * matb[1][0])
    posy = (mata[0][0] * matb[0][1] + mata[0][1] * matb[1][1])
    posz = (mata[1][0] * matb[0][0] + mata[1][1] * matb[1][0])
    posw = (mata[1][0] * matb[0][1] + mata[1][1] * matb[1][1])
    mata[0][0] = posx
    mata[0][1] = posy
    mata[1][0] = posz
    mata[1][1] = posw
 
def power(mata, num):
    """power"""
    if num == 0 or num == 1:
        return
    matb = [[1, 1], [1, 0]]
    power(mata, num // 2)
    multiply(mata, mata)
    if num % 2 != 0:
        multiply(mata, matb)
 
def main():
    """main docx"""
    num = int(input())
    print(fib(num))
 
main()
