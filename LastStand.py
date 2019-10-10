"""main"""
def main():
    """main docx"""
    import json
    raw = json.loads(input())
    _ = [print(str(i)[-1]) for i in raw]
 
main()
