"""main"""
def main():
    """main docx"""
    human = float(input())
    if human < 36:
        print("hypothermia")
    elif human < 38:
        print("No Fever")
    elif human < 39:
        print("Mild Fever")
    elif human < 40:
        print("High Fever")
    elif human >= 40:
        print("Very High Fever")
 
main()
