"""main"""
def main():
    """main funtion"""
    time = int(input())
    if time == 1:
        print("%.2f %.2f"%(float(input()), float(input()))) #จำนวนขนาดของขนมถ้ามี 1 ชิ้น ถือเป็นชิ้นที่คุ้มเลย
        return
    lst, lstdiff, lstpare = [], [], [] 
    iden = 0
    for _ in range(time * 2): #ลูปเก็บค่าทั้งหมดเข้า lst
        lst.append(abs(float(input())))
    for i in range(0, int(len(lst)), 2): #ลูปหารค่าทั้งหมดแล้วเก็บเข้า lstdiff
        lstdiff.append(lst[i+1] / lst[i])
        val = "%.2f %.2f"%(lst[i], lst[i+1])
        lstpare.append(val)
    for i in lstdiff: #ลูป lstpare เปรียบเทียบค่าจาก lst และ lstdiff เพื่อระบุจะได้เอามา print เฉย ๆ 
        if max(lstdiff) == i: 
            get = iden
        iden += 1
    print(lstpare[get]) #สรุป น้ำหนักสุทธิหารราคา ที่หารแล้วมีค่ามากที่สุดคือชิ้นที่คุ้ม***
 
main()
