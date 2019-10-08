"""Standard Sort Algorithms"""
def Selection_Sort(numbar):
    """selection sort"""
    for i in range(len(numbar)):
        small = i
        for j in range(i+1, len(numbar)):
            if numbar[small] > numbar[j]:
                small = j
        numbar[i], numbar[small] = numbar[small], numbar[i]
    return numbar

def Bubble_Sort(numbar):
    """bubble sort"""
    lenght = len(numbar)
    for i in range(lenght):
        for j in range(0, lenght-i-1):
            if numbar[j] > numbar[j+1]:
                numbar[j], numbar[j+1] = numbar[j+1], numbar[j]
    return numbar

def Insertion_Sort(numbar):
    """insertion sort"""
    for i in range(1, len(numbar)):
        key = numbar[i]
        tmp = i - 1
        while tmp >= 0 and key < numbar[tmp]:
            numbar[tmp + 1] = numbar[tmp]
            tmp -= 1
        numbar[tmp + 1] = key
    return numbar

def main():
    """input 8 numbers to sort"""
    numbar = [int(input()) for _ in range(8)]
    print(Insertion_Sort(numbar))

main()
