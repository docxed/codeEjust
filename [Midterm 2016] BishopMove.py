"""main"""
def direction(bhop, target):
    """iden direction"""
    if target[0] > bhop[0] and target[1] < bhop[1]:
        return "leftbot"
    elif target[0] < bhop[0] and target[1] < bhop[1]:
        return "lefttop"
    elif target[0] > bhop[0] and target[1] > bhop[1]:
        return "rightbot"
    elif target[0] < bhop[0] and target[1] > bhop[1]:
        return "righttop"

def main():
    """main docx"""
    field = [int(input())-1 for _ in range(2)] # กระดาน
    bhop = [int(input()) for _ in range(2)] # เรา
    other = [int(input()) for _ in range(2)] # ตัวอีกตัวนึง
    status = int(input()) # 0 เป็นมิตร 1 เป็นศัตรู
    target = [int(input()) for _ in range(2)] # เป้าหมาย***
    check = ""
    range_bt = abs(bhop[0]-target[0]) == abs(bhop[1]-target[1]) # ระยะเป้าหมาย
    range_bo = abs(bhop[0]-other[0]) == abs(bhop[1]-other[1]) # ระยะมิตร
    check += "P" if bhop[0]*bhop[1] <= field[0]*field[1] else "I" # ในกระดาน
    check += "I" if not range_bt else ""
    if range_bt and range_bo and direction(bhop, target) == direction(bhop, other):
        if abs(bhop[0]-other[0]) == abs(bhop[0]-target[0]):
            if status == 0:
                check += "I"
        elif abs(bhop[0]-other[0]) < abs(bhop[0]-target[0]):
            check += "I"
    print("No" if "I" in check else "Yes")

main()
