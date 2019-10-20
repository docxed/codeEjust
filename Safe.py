"""main"""
def main():
    """main docx"""
    code = [i for i in input()]
    crack = [i for i in input()]
    position = [i for i in range(len(code)) if code[i] != crack[i]]
    count = list()
    for i in position:
        first, defirst = code[i], crack[i]
        forward = abs(ord(first) - ord(defirst))
        if ord(first) <= ord(defirst):
            back = abs((ord(first)+26) - ord(defirst))
        else:
            back = abs((ord(defirst)+26) - ord(first))
        count.append(min(forward, back))
    print(sum(count))
 
main()
