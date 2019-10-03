"""main"""
def gold(world, lotto):
    """gold docx"""
    won = 0
    if lotto == world:
        won += 6000000
    if world == "000000":
        if lotto == "000001" or lotto == "999999":
            won += 100000
    elif world == "999999":
        if lotto == "999998" or lotto == "000000":
            won += 100000
    elif int(lotto) == int(world) - 1 or int(lotto) == int(world) + 1:
        won += 100000
    return won
 
def main():
    """main"""
    world = [input() for _ in range(6)]
    lotto = input()
    won = 0
    if lotto[4:6] == world[1]:
        won += 2000
    if lotto[0:3] == world[2]:
        won += 4000
    if lotto[0:3] == world[3]:
        won += 4000
    if lotto[3:6] == world[4]:
        won += 4000
    if lotto[3:6] == world[5]:
        won += 4000
    won += gold(world[0], lotto)
    print(won)
 
main()
