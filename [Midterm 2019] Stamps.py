"""main"""
def main():
    """main"""
    time = int(input()) # จำนวนครั้งที่บันทึกก่อนลดราคา
    pay = int(input()) # ราคาที่ใช้ได้กับโปรโมชัน
    givestamp = int(input()) # สแตมป์ที่ได้จากโปรฯ
    addstamp = int(input()) # จำนวนสแตมป์ที่สามารถใช้ลดราคา
    discount = int(input()) # ปริมาณราคาที่ลดให้
    stamp = 0
    world = [int(input()) for _ in range(time)] # บันทึกราคา
    for i in range(len(world)):
        if world[i] >= pay:
            count = world[i]
            while count >= pay:
                count -= pay
                stamp += givestamp
        while stamp >= addstamp:
            if i == len(world) - 1 or  world[i+1] == 0:
                break
            price = world[i+1] - discount
            world[i+1] = max(price, 0)
            stamp -= addstamp
    print(sum(world), stamp, sep="\n")
 
 
main()
