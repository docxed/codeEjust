"""
'นมขวดละ price บาท หากนำฝา b ฝา มาจะแลกได้ c ขวด และหากนำขวดเปล่ามา d ขวด จะแลกได้อีก e ขวด'
โจเองก็เห็นด้วยเพราะเป็นโปรโมชันที่ดูแปลกดี น่าจะเรียกลูกค้าได้เยอะ
แต่ติดปัญหานิดเดียวคือโจเองอยากรู้ว่าถ้าลูกค้ามีเงิน f บาท
"""


def main():
    """mpricein docx"""
    price = float(input())          # a
    cover = int(input())            # b
    cover_to_milk = int(input())    # c
    jar = int(input())              # d
    jar_to_milk = int(input())      # e
    money = float(input())          # f
    total, cap, bottle, total_pricell = 0, 0, 0, 0
    turn_cover, turn_jar, clock = True, True, True
    total += money // price
    cap += money // price
    while clock == True:
        clock = False
        while turn_cover == True:
            turn_cover = False
            if cap >= cover:
                cap -= cover
                cap += cover_to_milk
                total += cover_to_milk
                turn_cover = True
        bottle += total
        while turn_jar == True:
            turn_jar = False
            if bottle >= jar:
                bottle -= jar
                bottle += jar_to_milk
                cap += jar_to_milk
                total += jar_to_milk
                turn_jar = True
        total_pricell += total
        if cap >= cover:
            turn_cover, turn_jar, clock = True, True, True
            total = 0
    print("%d" % total_pricell)


main()
