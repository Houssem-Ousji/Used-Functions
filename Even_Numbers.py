def is_Even_Number(value):
    if value % 2 == 0:
        return True
    else:
        return False
def Even_Numbers(ivalue, fvalue):
    Even_Num = []
    for i in range(ivalue, fvalue+1):
        if is_Even_Number(i):
            Even_Num.append(i)
    return Even_Num
print(Even_Numbers(20, 50))
# return [20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50]