"""main"""
def goloop():
    """mafia loop"""
    stop = int(input())
    if stop == 0:
        print(0)
        return
    main(0, stop-1, 0, 1)
 
def main(current, stop, first, newfirst):
    """main docx"""
    if current == stop:
        print(newfirst)
        return
    new = first + newfirst
 
    main(current+1, stop, newfirst, new)
 
goloop()
