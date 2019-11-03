"""main"""
def main():
    """main docx"""
    # 2   1 1
    # 3   3 1+2
    # 4   6 1+2+3
    # 5   10 1+2+3+4
    # 6   15 1+2+3+4+5
    # ped = [int(input()) for _ in range(int(input()))]
    peddict = dict()
    for _ in range(int(input())):
        ped_input = int(input())
        peddict[ped_input] = peddict.get(ped_input, 0) + 1
        # print(peddict)
    k = int(input())
    ans = 0
    uniqped = [i for i in set(peddict) if i < k/2]
    for i in uniqped:
        ans += peddict.get(i, 0) * peddict.get(k-i, 0)
    ans += sum(range(1, peddict.get(k/2, 0)))
    print(ans)

main()
