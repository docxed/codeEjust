"""main"""
import math as m
def fucn(num):
    """catalan"""
    return m.factorial((2 * num)) / (m.factorial(num + 1) * m.factorial(num))
def main():
    """main docxed"""
    num = int(input())
    print(int(fucn(num)))
 
 
main()
