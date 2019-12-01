"""main"""


def convert_int(raw):
    """convert str to int"""
    raw = [int(raw[1]), int(raw[2]), int(raw[3]), raw[0]]
    return raw


def main():
    """main docx"""
    raw = sorted([input().split()
                  for _ in range(int(input()))], key=convert_int, reverse=True)
    lenght = len(raw)
    for i in range(lenght):
        for j in range(0, lenght-i-1):
            if raw[j][1:] == raw[j+1][1:]:
                if raw[j][0] > raw[j+1][0]:
                    raw[j], raw[j+1] = raw[j+1], raw[j]
    keep = None
    for rank in range(len(raw)):
        ranking = rank + 1
        medals = raw[rank][1] + raw[rank][2] + raw[rank][3]
        if medals == keep:
            pass
        else:
            ranked = ranking
        keep = medals
        print(
            ranked, raw[rank][0], raw[rank][1], raw[rank][2], raw[rank][3], int(
                raw[rank][1]) + int(raw[rank][2]) + int(raw[rank][3])
        )


main()
