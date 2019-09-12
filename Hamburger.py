"""main"""
def main():
    """main function"""
    pipe, star = int(input()), int(input())
    print("|"*pipe + "*"*((pipe+star)*2) + "|"*star)

main()
