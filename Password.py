"""main"""
def main():
    """main docx"""
    import hashlib
    print(hashlib.sha512(input().encode()).hexdigest().upper())
 
main()
