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
    code = int(input())
    txt = [i for i in input()]
    last = []
    for i in txt:
        last.append(decode(i, code))
    print("".join(last))
 
main()
