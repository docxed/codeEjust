"""main"""
def main():
    """min docx"""
    ratea, rateb, team = int(input()), int(input()), input()
    if team == "A":
        res = (1)/(1+10**((rateb-ratea)/400))
    else:
        res = (1)/(1+10**((ratea-rateb)/400))
    print("%.2f"%res)
 
main()
