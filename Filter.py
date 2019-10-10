"""main"""
def main():
    """main docx"""
    import json
    txt = json.loads(input())
    lim = float(input())
    human = [i for i in txt]
    human = sorted(list(filter(lambda num: int(txt[num]) >= lim, human)))
    if human == []:
        print("Nope")
        return
    _ = [print(human[i], "%.2f"%txt[human[i]], sep="\t") for i in range(len(human))]
 
main()
