"""main"""
def whom():
    """process docx"""
    minute = float(input())
    book = sorted([float(input()) for _ in range(int(input()))])
    finished, read = 0, 0
    for i in range(len(book)):
        if read + book[i] > minute:
            break
        if read < minute:
            read += book[i]
            finished += 1
    print(finished)
 
def main():
    """main docx"""
    for _ in range(int(input())):
        whom()
 
main()