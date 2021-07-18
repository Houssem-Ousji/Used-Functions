def is_Odd_Number(value):
    if value % 2 != 0:
        return True
    else:
        return False
def Odd_Numbers(ivalue, fvalue):
    Odd_Num = []
    for i in range (ivalue, fvalue+1):
        if is_Odd_Number(i):
            Odd_Num.append(i)
    return Odd_Num
print(Odd_Numbers(20,50))
# return [21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49]