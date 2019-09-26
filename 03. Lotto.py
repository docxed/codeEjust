"""main"""
def fix(world, lotto):
    """fix"""
    won = 0
    if lotto == "000000":
        won += 6000000
    elif lotto == "000001" or lotto == "999999":
        won += 100000
    elif lotto == "999999":
        won += 6000000
    elif lotto == "000001" or lotto == "999998":
        won += 100000
    return won

def gold(world, lotto):
    """gold"""
    if world == "000000" or world == "999999":
        return fix(world, lotto)
    won = 0
    lotto = int(lotto)
    world = int(world)
    if lotto == world:
        won += 6000000
    if lotto == world - 1 or lotto == world + 1:
        won += 100000
    return won

def main():
    """main"""
    world = [input() for _ in range(6)]
    lotto = input()
    won = 0
    if lotto == world[1]: #เลขท้าย 2 ตัว
        won += 2000
    if lotto[0:3] == world[2]: #เลขหน้า 3 ตัว
        won += 4000
    if lotto[0:3] == world[3]: #เลขหน้า 3 ตัว
        won += 4000
    if lotto[3:6] == world[4]: #เลขท้าย 3 ตัว
        won += 4000
    if lotto[3:6] == world[5]: #เลขท้าย 3 ตัว
        won += 4000
    won += gold(world[0], lotto) #รางวัลที่ 1
    print(won)

main()
