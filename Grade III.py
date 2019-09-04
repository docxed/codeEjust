"""main"""
def main():
    """main function"""
    time = int(input())
    grade = 0
    for _ in range(time):
        score = float(input())
        if 95 <= score <= 100:
            grade += 4
        elif 90 <= score < 95:
            grade += 3.5
        elif 85 <= score < 90:
            grade += 3
        elif 80 <= score < 85:
            grade += 2.5
        elif 75 <= score < 80:
            grade += 2
        elif 70 <= score < 75:
            grade += 1.5
        elif 65 <= score < 70:
            grade += 1
        elif 60 <= score < 65:
            grade += 0.5
        else:
            grade += 0
    res = grade / time
    res = int(res*100) / 100
    print("%.2f"%res)
 
main()
