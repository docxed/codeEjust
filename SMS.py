"""main"""
def del_char(word, time):
    """delete char"""
    for _ in range(time):
        if word != []:
            word.pop()
    return word

def main():
    """main docx"""
    lenght = int(input())
    word = []
    cnt = 0
    while cnt != lenght:
        num, time = int(input()), int(input())
        if num == 1:
            word = del_char(word, time)
        elif num == 2:
            alphabet = "ABC"
            word.append(alphabet[time%3 - 1])
        elif num == 3:
            alphabet = "DEF"
            word.append(alphabet[time%3 - 1])
        elif num == 4:
            alphabet = "GHI"
            word.append(alphabet[time%3 - 1])
        elif num == 5:
            alphabet = "JKL"
            word.append(alphabet[time%3 - 1])
        elif num == 6:
            alphabet = "MNO"
            word.append(alphabet[time%3 - 1])
        elif num == 7:
            alphabet = "PQRS"
            word.append(alphabet[time%4 - 1])
        elif num == 8:
            alphabet = "TUV"
            word.append(alphabet[time%3 - 1])
        elif num == 9:
            alphabet = "WXYZ"
            word.append(alphabet[time%4 - 1])
        cnt += 1
    print(*word if word != [] else "null", sep="")

main()
