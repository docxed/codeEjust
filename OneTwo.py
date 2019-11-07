"""main"""
def main():
    """string concate is poor way but list slicing is better one"""
    num = int(input())
    if num >= 3:
        list1, list2 = [num], []
        while list1 != []:
            first = list1[0]
            list1.pop(0)
            if first == 2:
                list2.append(first)
            else:
                val1 = first - 1
                if val1 == 2:
                    list2.append(val1)
                else:
                    list1.insert(0, val1)
                val2 = first - 2
                if val2 == 1:
                    list2.append(val2)
                else:
                    list1.insert(1, val2)
        print(*list2, sep="")
    elif num == 1:
        print(1)
    elif num == 2:
        print(2)

main()
