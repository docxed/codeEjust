"""main"""
import json


def main():
    """BBB"""
    atk = sorted(list(json.loads(input())), reverse=True)
    dfn = sorted(list(json.loads(input())), reverse=True)
    total = 0
    while atk != []:
        pivot = dfn.pop(0)
        if atk[0] > pivot:
            total += atk[0]
            atk.pop(0)
        else:
            atk.pop()
    print(total)


main()
