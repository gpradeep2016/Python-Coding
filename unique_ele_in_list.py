def unique_element(input_list):
    x = []
    for i in input_list:
        if i not in x:
            x.append(i)
    print x


unique_element([1, 2, 2, 2, 3, 4,4])