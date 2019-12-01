"""main"""
import json


def main():
    """main docx"""
    evar = input().replace("'", "\"")
    data = [input()]
    raw = json.loads(evar)
    collect, trash = [data[0]], list()
    while data != []:
        extract = raw[data[0]]
        collect.extend(extract)
        trash.append(data[0])
        for i in extract:
            if i not in trash:
                data.append(i)
        data.pop(0)
    print(sorted(set(collect)))


main()
