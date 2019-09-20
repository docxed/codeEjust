"""main"""
def sording1(world):
    """slide sord low"""
    for i in range(len(world)):
        small = i
        for j in range(i+1, len(world)):
            if world[small] > world[j]:
                small = j
        world[i], world[small] = world[small], world[i]
    return world
 
def sording2(world):
    """slide sord high"""
    for i in range(len(world)):
        small = i
        for j in range(i+1, len(world)):
            if world[small] < world[j]:
                small = j
        world[i], world[small] = world[small], world[i]
    return world
 
def main():
    """main docx"""
    end = input()
    point, used = 0, 0
    while True:
        if int(end) == 6174:
            print(point)
            break
        else:
            end = str(end)
            end = [int(i) for i in end]
            diff_1, diff_2 = int("".join(map(str, sording2(end)))),\
                 int("".join(map(str, sording1(end))))
            end = diff_1 - diff_2
            if len(str(end)) < 4 and used == 0:
                end = str(end)
                end += "0"
                used += 1
            point += 1
 
main()
