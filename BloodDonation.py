"""main"""
def main():
    """main docx"""
    age = int(input())
    weight = int(input())
    time = int(input())
    check = ""
    check += "P" if 17 <= age <= 70 else "I" # age
    check += "P" if weight >= 45 else "I" # weight
    if time == 0:
        if age <= 55:
            check += "P"
        else:
            check += "I"
    else:
        check += "P"
    if age == 17 or 60 <= age <= 70:
        accept = input()
        check += "P" if accept == "True" else "I"
    print("No" if "I" in check else "Yes")

main()
