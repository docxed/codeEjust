"""main"""
def funcy(point):
    """return y"""
    return point[1]

def funcx(point):
    """return x + y"""
    return point[0] + point[1]

def process():
    """process exam"""
    size = int(input())
    raw = [list(map(int, input().split())) for _ in range(size)]
    sortx = sorted(raw, key=funcx) # [[2, 4], [4, 2], [10, 0], [1, 9]]
    axised = list(map(funcx, sortx)) # [6, 6, 10, 10]
    diff, worst = [], [] # [6, 10]
    for i in axised: # make order
        if i not in diff:
            diff.append(i)
    for i in range(len(diff)):
        if axised.count(diff[i]) > 1:
            worst.append(diff[i])
    fixy, ans = [], []
    while sortx != []:
        if sum(sortx[0]) in worst:
            fixy.append(sortx[0])
        else:
            fixy = sorted(fixy, key=funcy, reverse=True)
            ans.extend(fixy)
            ans.append(sortx[0])
            fixy.clear()
        sortx.pop(0)
    if fixy != []:
        fixy = sorted(fixy, key=funcy, reverse=True)
        ans.extend(fixy)
    _ = [print(*i) for i in ans]

def main():
    """main docx"""
    amount = int(input())
    for _ in range(amount):
        process()

main()
