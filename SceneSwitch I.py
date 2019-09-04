"""main"""
def tock(tick):
    """Find Even and Odd"""
    if (tick+1) % 2 == 1:
        return True
    return False
 
def main():
    """main function"""
    tick = light = state = mode = 0
    while True:
        raw = input()
        if raw == "End":
            break
        else:
            tick = tock(tick)
            if tick:
                if float(raw) - state > 6:
                    mode = 0
                light += mode
                mode = tock(mode)
        state = float(raw)
    print(light)
 
main()
