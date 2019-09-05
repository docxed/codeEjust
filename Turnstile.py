"""main"""
def main():
    """main funtion"""
    sumtxt = ""
    while 1:
        txt = input()
        if txt == "END":
            break
        sumtxt += txt
    print(sumtxt.count("CP"))
 
main()
