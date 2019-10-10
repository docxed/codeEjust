"""main"""
def main():
    """main docx"""
    time = int(input())
    raw = [input().split("\t") for _ in range(time)]
    score = [float(raw[i][1]) for i in range(len(raw))]
    avg = sum(score) / len(score)
    near = [[raw[i][0], float(raw[i][1])] for i in range(len(raw)) if float(raw[i][1]) <= avg]
    nearer = [[near[i][0], abs(near[i][1] - avg)] for i in range(len(near))]
    deep = [nearer[i][1] for i in range(len(nearer))]
    print(*near[deep.index(min(deep))], sep="\t")
 
main()
