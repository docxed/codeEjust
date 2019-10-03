"""main"""
def main():
    """main"""
    guess, pick = input(), input()
    guess, pick = [i for i in guess], [i for i in pick]
    board = list()
    for i in range(len(guess)):
        if guess[i] == pick[i]:
            board.append("B")
            guess[i] = "-"
            pick[i] = "-"
    for _ in range(guess.count("-")):
        guess.remove("-")
        pick.remove("-")
    for j in range(len(pick)):
        if pick[j] in guess:
            board.append("W")
            guess.remove(pick[j])
    while len(board) < 4:
        board.append("O")
    print(*board, sep="")
 
main()
