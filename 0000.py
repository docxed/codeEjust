"""main"""
def main():
    """main docx"""
    size = int(input())
    stop, pause = 0, 0
    col, row = 0, 1
    out, cout = 0, 1
    stage = 0
    while stop < size:
        out, cout = 0, 1
        while pause < size:
            if col + row > size:
                stage = 1
                print(out + cout, end=" ")
            else:
                stage = 0
                print(
                    col + row, end=" "
                )
            if stage == 1:
                cout += 1
            pause += 1
            row += 1
        print()
        pause, row = 0, 1
        stop += 1
        col += 1
        if stage == 1:
            out += 1

main()
