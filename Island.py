"""count island with DFS"""
def count_houses(matrix, visited, i, j):
    """count house"""
    if i < 0 or i >= len(matrix) or j < 0 or j >= len(matrix[0]) or\
            visited[i][j] is True or matrix[i][j] == 0:
        return 0
    visited[i][j] = True
    cnt = 1
    for raw in range(i-1, i+2, 1):
        for cal in range(j-1, j+2, 1):
            if raw != i or cal != j:
                cnt += count_houses(matrix, visited, raw, cal)
    return cnt

def island_count(matrix):
    """count island"""
    clusters = 0
    row = len(matrix)
    col = len(matrix[0])
    visited = [[False for i in range(col)] for j in range(row)]
    for i in range(row):
        for j in range(col):
            if matrix[i][j] == 1 and visited[i][j] is False:
                clusters += 1
                count_houses(matrix, visited, i, j)
    return clusters

def main():
    """main docx"""
    lenght = list(map(int, input().split()))
    matrix = [list(map(int, input().split())) for _ in range(lenght[0])]
    clusters = island_count(matrix)
    print(clusters)

main()
