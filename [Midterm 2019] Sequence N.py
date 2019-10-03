"""main"""
def main():
    """min docx"""
    size = int(input())
    for i in range(size):
        if i == 0 or i == size - 1:
            print("*" + " "*(size-2) + "*")
        else:
            print(
                "*" + " "*(i-1) + "*" + " "*(size-2-i) + "*"
            )
 
main()
