"""main"""
def is_yes(number, raw):
    """progress YES"""
    if raw[0] == ">":
        number = [i for i in number if i > raw[1]]
    elif raw[0] == "<":
        number = [i for i in number if i < raw[1]]
    elif raw[0] == "=":
        number = [raw[1]]
    return number
 
def is_no(number, raw):
    """progress NO"""
    if raw[0] == ">":
        number = [i for i in number if i <= raw[1]]
    elif raw[0] == "<":
        number = [i for i in number if i >= raw[1]]
    elif raw[0] == "=" and (raw[1] in number):
        number.remove(raw[1])
    return number
 
def main():
    """main docx"""
    number = [i for i in range(0, 100+1)]
    while 1:
        raw = input().split()
        if raw[0] == "END":
            break
        raw[1] = int(raw[1])
        if raw[2] == "YES":
            number = is_yes(number, raw)
        elif raw[2] == "NO":
            number = is_no(number, raw)
    print(*number, sep=" ")
 
main()