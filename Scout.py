"""main"""
def process(_, lim, weight):
    """process docx"""
    egg = sorted(list(map(float, input().split())))
    gram, foam = 0, 0
    for i in egg:
        gram += i
        foam += 1
        if gram > weight or foam > lim:
            gram -= i
            foam -= 1
            break
    print(foam)


def main():
    """main docx"""
    for _ in range(int(input())):
        bipot = list(map(int, input().split()))
        process(bipot[0], bipot[1], bipot[2])

main()
