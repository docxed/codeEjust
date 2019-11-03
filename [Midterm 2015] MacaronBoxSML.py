"""main"""
def main():
    """main docx"""
    desert = int(input())
    high, medium, small = 0, 0, 0
    high += desert // 24
    desert %= 24
    if desert > 12:
        high += 1
        desert = desert - 12
    elif 6 < desert <= 12:
        medium += 1
        desert %= 12
    elif 0 < desert <= 6:
        small += 1
    print(small, medium, high, sep="\n")

main()
