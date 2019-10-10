"""main"""
def main():
    """main docx"""
    import statistics
    time = int(input())
    lst = [int(input()) for _ in range(time)]
    print("%.1f"%statistics.median(lst))
 
main()
