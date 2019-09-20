"""Main program"""
def main():
    """main docsting"""
    num = int(input())
    loop_num = num - 1
    point = 2
    print(" "*((num)*2-2) + "%02d"%(num))
    for i in range(loop_num):
        print(" "*((loop_num-i)*2-2) + "%02d"%(loop_num-i) \
        + " "*(point) + "%02d"%(loop_num-i))
        point += 4
 
main()
