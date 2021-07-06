# condition: Sorted list

# function to check is a sorted list or Not
def is_sorted(My_List):
    Another_List = sorted(My_List)
    sorted_list = True
    n = len(My_List) # or Another list us you like
    i = 0
    while i < n and sorted_list:
        if My_List[i] != Another_List[i]:
            sorted_list = False
        i += 1
    return sorted_list

# The Binary search
def binary_search(My_List, x):
    if is_sorted(My_List):
        n = len(My_List)
        exist = False
        while n > 0 and exist == False:
            if x == My_List[n // 2]:
                exist = True
            elif x > My_List[n // 2]:
                My_List = My_List[(n // 2) + 1:]
            elif x < My_List[n // 2]:
                My_List = My_List[:(n // 2)]
            n = len(My_List)
        return (exist)
    else:
        error = "Your List doesn't Satisfied The Condition"
        return (error)

example_1 = [14, 12, 125, 4, 69, 258]
print(binary_search(example_1, 14)) #the second parameter doesn't effect anything
# output : Your List doesn't Satisfied The Condition

example_2 = [15, 22, 32, 66, 124, 255, 963, 1045]
print(binary_search(example_2, 100))
# output : False

example_3 = [15, 22, 32, 66, 124, 255, 963, 1045]
print(binary_search(example_2, 255))
# output : True