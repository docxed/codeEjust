"""main"""
def main():
    """main docx"""
    txt = [input() for i in range(int(input()))]
    wrong = ['if', 'else', 'elif', 'while', 'for', 'True', 'False', 'continue', 'None'\
, 'break', 'return', 'is', 'in', 'and', 'or', 'from', 'as', 'pass', 'not', 'def']
    while txt != []:
        test = txt[0]
        check = ""
        one = test
        for _ in range(one.count("_")):
            one = one.replace("_", "")
        for i in one:
            if not i.isalnum():
                check += "I"
        two = [i for i in test]
        if two[0] == ' ':
            two.pop(0)
        if two[-1] == ' ':
            two.pop()
        if ' ' in two:
            check += "I"
        three = test
        if three[0].isdigit():
            check += "I"
        four = test
        for i in wrong:
            if i == four:
                check += "I"
                break
        txt.pop(0)
        print("Invalid" if "I" in check else "Valid")

main()
