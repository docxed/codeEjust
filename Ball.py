"""main"""
def main():
    """main docx"""
    ball = float(input())
    cnt = -1
    while ball > 0.01:
        ball *= 0.6
        cnt += 1
    print(max(0, cnt))

main()
