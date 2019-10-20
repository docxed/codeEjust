"""main"""
def main():
    """main docx"""
    text = [input() for _ in range(int(input()))]
    lenght = [len(i) for i in text]
    _ = [print(text[lenght.index(i)]) for i in sorted(lenght)]
 
main()
