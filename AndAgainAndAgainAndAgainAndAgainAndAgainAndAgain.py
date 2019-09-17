"""main"""
def main():
    """main doc"""
    world_txt, abandon_txt, get = str(), str(), 0
    bucket = "aeiouAEIOU"
    for i in input():
        if i == " " or i == ".":
            for j in abandon_txt:
                if j in bucket:
                    get += 1
            if get >= 2:
                get = 0
                world_txt += abandon_txt + " "
                abandon_txt = str()
            else:
                get, abandon_txt = 0, str()
        else:
            abandon_txt += i
    world_txt, get = list(sorted(world_txt.split())), None
    for j in world_txt:
        if j.isalpha():
            get = True
    if get == None:
        print("Nope")
    else:
        _ = [print(k) for k in world_txt]
 
main()
