"""main"""
def main():
    """main docx"""
    level = int(input())
    current = int(input())
    while 1:
        txt = input()
        if txt == "END":
            break
        if txt == "UP":
            current += 1
        else:
            current -= 1
        if current > level:
            current = level
        elif current < 1:
            current = 1
    print(current)

main()
