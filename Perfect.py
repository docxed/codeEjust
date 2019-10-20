"""main"""
def main():
    """main docx"""
    end = int(input())
    divisors, proper = [1], []
    for i in range(6, end+1):
        for j in range(2, int(i**.5)+1):
            if i % j == 0:
                divisors.append(j + (i//j))
        if sum(divisors) == i:
            proper.append(i)
        divisors = [1]
    print(sum(proper))
 
main()
