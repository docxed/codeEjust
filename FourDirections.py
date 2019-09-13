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
    _ = [print("  *  ", end=" ") for _ in raw]
    print()
    _ = [print(level_1[i], end=" ") for i in raw]
    print()
    _ = [print(level_2[i], end=" ") for i in raw]
    print()
    _ = [print(level_3[i], end=" ") for i in raw]
    print()
    _ = [print("  *  ", end=" ") for _ in raw]

main()
