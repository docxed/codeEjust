"""main"""
def main():
    """main func"""
    lst = []
    alice, bob, ice = int(input()), int(input()), int(input())
    world_alice = abs(ice - alice)
    lst.append(world_alice)
    world_bob = abs(ice - bob)
    lst.append(world_bob)
    if lst[0] < lst[1]:
        print("Alice", lst[0])
    if lst[1] < lst[0]:
        print("Bob", lst[1])
    if lst[0] == lst[1]:
        print("Sundaes", lst[0])
 
main()
