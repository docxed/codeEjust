"""main"""
def main():
    """main docx"""
    txt = input()
    lenght = len(txt) - 1
    size = 1
    for _ in range(len(txt)):
        print(
            " "*(lenght) + txt[0:size]
            )
        lenght -= 1
        size += 1
    size = 1
    for _ in range(len(txt) - 1):
        print(
            txt[size:]
            )
        size += 1

main()
