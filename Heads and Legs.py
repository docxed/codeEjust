"""main"""
def main():
    """main docx"""
    animal = int(input()) # a
    legs = int(input()) # b
    bird = (animal*4-legs) / 2
    high = animal * 4
    low = animal * 2
    bunny = animal - bird
    if legs > high or legs < low or legs % 2 != 0:
        print("Impossible")
    else:
        print("%d %d"%(bunny, bird))
 
main()