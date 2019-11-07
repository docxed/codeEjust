"""main"""
def kel(cel):
    """celcius to kelvin"""
    return cel + 273.15
 
def fah(cel):
    """celcius to fahrenheit"""
    return cel * (9/5) + 32
 
def ran(cel):
    """celcius to rank"""
    return (cel + 273.15) * (9/5)
 
 
def main():
    """main docx"""
    data = float(input())
    lite = input()
    lited = input()
    if lite == "F":
        data = (data - 32) * (5/9)
    elif lite == "K":
        data = data - 273.15
    elif lite == "R":
        data = (data - 491.67) * (5/9)
    if lited == "K":
        print("%.2f"%kel(data))
    elif lited == "F":
        print("%.2f"%fah(data))
    elif lited == "R":
        print("%.2f"%ran(data))
    else:
        print("%.2f"%data)

main()
