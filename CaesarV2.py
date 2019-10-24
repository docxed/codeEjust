"""main"""
def decode(char, code):
    """decode"""
    if "A" <= char <= "Z":
        conv = ord(char) + code
        while conv < 65:
            conv += 26
        while conv > 90:
            conv -= 26
        return chr(conv)
    elif "a" <= char <= "z":
        conv = ord(char) + code
        while conv < 97:
            conv += 26
        while conv > 122:
            conv -= 26
        return chr(conv)
    else:
        return char
 
def main():
    """main docxed"""
    txt = [i for i in input()]
    code = 0
    while 1:
        code += 1
        last = []
        for i in txt:
            last.append(decode(i, code))
        if "the" in "".join(last).lower():
            print("".join(last))
            break

main()
