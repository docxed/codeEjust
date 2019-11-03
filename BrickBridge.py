"""main"""
def brick():
    """main docx"""
    brick_a = int(input())# *1
    brick_b = int(input())# *5
    goal = int(input())
    brick_b_need = goal//5
    if brick_b >= brick_b_need:
        brick_left = goal-(brick_b_need*5)
    else:
        brick_left = goal-(brick_b*5)
    print(brick_left if brick_a >= brick_left else "-1")

brick()
