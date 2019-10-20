"""main"""
def main():
    """main docx"""
    txt = input()
    clone = ""
    turn = True
    for i in txt:
        if i == "<":
            turn = None
        elif i == ">":
            clone += " "
            turn = True
        elif turn == True:
            clone += i
    print(clone.split())
 
main()
