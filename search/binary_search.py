def binary_search(My_List, x):
    n = len(My_List)
    exist = False
    while n > 0 and exist == False:
        if x == My_List[n//2]:
            exist = True
        elif x > My_List[n//2]:
            My_List = My_List[(n//2)+1:]
        elif x < My_List[n//2]:
            My_List = My_List[:(n//2)]
        n = len(My_List)
    return (exist)
