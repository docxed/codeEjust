"""main"""
def main():
    """main docx"""
    hole = int(input())
    position = int(input())
    pigeonhole = [list(map(int, input().split())) for _ in range(hole)]
    diamond_bag, count = [], []
    for i in range(position):
        for j in range(len(pigeonhole)):
            count.append(pigeonhole[j][i])
        diamond_bag.append(sum(count))
        count.clear()
    print(max(diamond_bag))
 
main()
