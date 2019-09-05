"""main"""
def main():
    """main funtion"""
    virus = input()
    cnt = 0
    for i in virus:
        if i == "o":
            cnt += 1
    print(cnt)
 
main()
