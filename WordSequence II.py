"""main"""
def main():
    """main docx"""
    old = input()
    new = input()
    slidenew, slideold = 0, 0
    loop = max(len(old), len(new)) + 1
    for _ in range(loop):
        print(new[0:slidenew] + old[slideold:len(old)])
        slidenew += 1
        slideold += 1
 
main()
