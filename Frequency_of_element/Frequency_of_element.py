string_1 = 'aaalvddallla'

def find_frequency(string_a):
    counter_dict = {}
    for ele in string_a:
        if ele not in counter_dict:
            counter_dict[ele] = 0
        counter_dict[ele] += 1

    print(counter_dict)

find_frequency(string_1)
