"""main"""
import json
def main():
    """main docx"""
    distance = int(input())
    human = json.loads(input())
    cnt = 0
    while human != []:
        rad = min(human)
        rad += distance*2
        human = [i for i in human if i > rad]
        cnt += 1
    print(cnt)

main()
