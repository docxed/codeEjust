"""XOXO"""
def row(tictac):
    """check row"""
    turn = True
    for i in tictac:
        if i == "OOO":
            print("O WIN")
            turn = False
            break
        elif i == "XXX":
            print("X WIN")
            turn = False
            break
    return turn
 
def col(tictac):
    """check col"""
    turn = True
    keep = ""
    for i in range(3):
        for j in range(3):
            keep += tictac[j][i]
        if keep == "OOO":
            print("O WIN")
            turn = False
            break
        elif keep == "XXX":
            print("X WIN")
            turn = False
            break
        keep = ""
    return turn
 
def det_left_to_right(tictac):
    """check det left to right"""
    turn = True
    keep = ""
    pos = 0
    for i in range(3):
        keep += tictac[i][pos]
        pos += 1
        if keep == "OOO":
            print("O WIN")
            turn = False
            break
        elif keep == "XXX":
            print("X WIN")
            turn = False
            break
    return turn
 
def det_right_to_left(tictac):
    """check det right to left"""
    turn = True
    keep = ""
    pos = 2
    for i in range(3):
        keep += tictac[i][pos]
        pos -= 1
        if keep == "OOO":
            print("O WIN")
            turn = False
            break
        elif keep == "XXX":
            print("X WIN")
            turn = False
            break
    return turn
 
def main():
    """XOXO"""
    tictac = [input() for _ in range(3)]
    # นอน
    turn = row(tictac)
    if turn == False:
        return
    # ตั้ง
    turn = col(tictac)
    if turn == False:
        return
    # เฉียงซ้ายไปขวา
    turn = det_left_to_right(tictac)
    if turn == False:
        return
    # เฉียงขวาไปซ้าย
    turn = det_right_to_left(tictac)
    if turn == False:
        return
    print("DRAW")
 
main()