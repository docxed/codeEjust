"""main"""
def main():
    """main funtion"""
    lst = []
    point = 0
    for _ in range(int(input())):
        card = input()
        lst.append(card)
    for i in lst:
        if i == "J" or i == "Q" or i == "K":
            point += 10
        elif i == "A":
            point += 11
        else:
            point += int(i)
        if point > 21 and "A" in lst and point <= 30:
            point -= 10
        elif point > 30 and "A" in lst:
            point -= 10
    print(point)
 
main()
