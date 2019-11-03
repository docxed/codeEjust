"""main"""
def invert(num):
    """invert"""
    if num == '0':
        return '1'
    return '0'
 
def main():
    """main docx"""
    raw = [i for i in input()]
    num = list(map(invert, raw))
    res = int(''.join(num))
    if res != 0:
        print(res)

main()
