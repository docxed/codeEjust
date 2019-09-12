"""main"""
def main():
    """main function"""
    pos = input().upper()
    pos1, pos2, pos3 = "*", "", ""
    for i in pos:
        if i == 'A':
            numx = pos1
            numy = pos2
            pos1 = pos1.replace(pos1, numy)
            pos2 = pos2.replace(pos2, numx)
        elif i == 'B':
            numx = pos2
            numy = pos3
            pos2 = pos2.replace(pos2, numy)
            pos3 = pos3.replace(pos3, numx)
        elif i == 'C':
            numx = pos1
            numy = pos3
            pos1 = pos1.replace(pos1, numy)
            pos3 = pos3.replace(pos3, numx)
    if pos1 == '*':
        print('1')
    elif pos2 == '*':
        print('2')
    elif pos3 == '*':
        print('3')
 
main()
