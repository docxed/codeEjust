"""main"""
def main():
    """main"""
    import json
    raw = json.loads(input())
    turn = True
    last, con = [], []
    while turn == True:
        turn = False
        for i in raw:
            if isinstance(i, int):
                last.append(i)
            elif isinstance(i, list):
                con += i
                turn = True
        if con == []:
            turn = False
        raw = con.copy()
        con.clear()
    print(sorted(last, reverse=True))
 
main()
