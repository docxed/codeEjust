"""main"""
def main():
    """main docx"""
    kabata = [input() for _ in range(int(input()))]
    for i in kabata:
        if "baka" in i:
            print("no")
        else:
            for _ in range(i.count("bakka")):
                i = i.replace("bakka", "-")
            for _ in range(i.count("ka")):
                i = i.replace("ka", "-")
            for _ in range(i.count("ba")):
                i = i.replace("ba", "-")
            for _ in range(i.count("ta")):
                i = i.replace("ta", "-")
            for _ in range(i.count("-")):
                i = i.replace("-", "")
            if i != "":
                print("no")
            else:
                print("yes")
 
main()
