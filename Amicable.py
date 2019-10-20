"""main"""
def main():
    """main docx"""
    end = int(input())
    first_vector, second_vector, amicable = [1], [1], []
    for number in range(1, end+1):
        for vector in range(2, int(number**.5)+1):
            if number % vector == 0:
                first_vector.append(vector + (number//vector))
        diff_num = sum(first_vector)
        for dvector in range(2, int(diff_num**.5)+1):
            if diff_num % dvector == 0:
                second_vector.append(dvector + (diff_num//dvector))
        ami = sum(second_vector)
        if ami == number and number not in amicable and diff_num not in amicable:
            amicable.append(number)
            amicable.append(diff_num)
        first_vector, second_vector = [1], [1]
    decode_amicable = amicable.copy()
    amicable.clear()
    _ = [print(sum([i for i in decode_amicable if decode_amicable.count(i) == 1]))]
 
main()
