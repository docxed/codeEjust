"""main"""
def main():
    """main docx"""
    rodict = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    roman = input()
    val = 0
    if "IV" in roman or "IX" in roman:
        val -= 2
    if "XL" in roman or "XC" in roman:
        val -= 20
    if "CD" in roman or "CM" in roman:
        val -= 200
    for i in roman:
        val += rodict[i]
    print(val)

main()
