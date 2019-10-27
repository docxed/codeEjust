"""main"""
import hashlib
 
def main():
    """main docx"""
    txt = input().lower()
    for i in range(0, 99999+1):
        decrypt = "%05d"%i
        diff = hashlib.sha512(decrypt.encode()).hexdigest()
        if diff == txt:
            print(decrypt)
            break
 
main()