"""main"""
def main():
    """main docx"""
    num1, num2, num3, world_method = int(input()), int(input()), int(input()), list()
    if num1 >= 0 and num2 >= 0 and num3 >= 0:
        world_method.append("%d%d%d"%(num1, num2, num3))
        world_method.append("%d%d%d"%(num1, num3, num2))
        world_method.append("%d%d%d"%(num2, num1, num3))
        world_method.append("%d%d%d"%(num2, num3, num1))
        world_method.append("%d%d%d"%(num3, num1, num2))
        world_method.append("%d%d%d"%(num3, num2, num1))
        world_method = list(map(int, world_method))
        for i in range(len(world_method)): #slide sording
            tiny = i
            for j in range(i+1, len(world_method)):
                if world_method[i] > world_method[j]:
                    tiny = j
            world_method[i], world_method[tiny] = world_method[tiny], world_method[i]
        world_method = list(map(str, world_method))
        print(world_method[-1])
 
main()
