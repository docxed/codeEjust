"""main"""
def main():
    """main docx"""
    _ = int(input())
    food = list(map(int, input().split()))
    day = 1
    while 0 not in food:
        keep = food.index(min(food))
        for i in range(len(food)):
            food[i] -= 1
        food[keep] += 1
        day += 1
    print(day-1)
 
 
main()