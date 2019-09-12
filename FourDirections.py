"""main"""
def main():
    """main function"""
    raw = input().lower()
    level_1 = {
        "u": " *** ",
        "d": "  *  ",
        "l": " *   ",
        "r": "   * "
    }
    level_2 = {
        "u": "* * *",
        "d": "* * *",
        "l": "*****",
        "r": "*****"
    }
    level_3 = {
        "u": "  *  ",
        "d": " *** ",
        "l": " *   ",
        "r": "   * "
    }

    for _ in raw: #onframe
        print("  *  ", end=" ")
    print()
    for i in raw: #level_1
        print(level_1[i], end=" ")
    print()
    for i in raw: #level_2
        print(level_2[i], end=" ")
    print()
    for i in raw: #level_3
        print(level_3[i], end=" ")
    print()
    for _ in raw: #framingframe
        print("  *  ", end=" ")
    print()

main()
