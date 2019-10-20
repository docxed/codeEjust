"""main"""
def main(gang_a, gang_b):
    """main docx"""
    res = list({int(input()) for _ in range(gang_a)} & {int(input()) for _ in range(gang_b)})
    if res == []:
        return print("Nope")
    print(*sorted(res, reverse=True), sep="\n")
 
main(int(input()), int(input()))
