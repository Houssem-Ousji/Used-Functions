def is_Narcissistic_Number(value):
    if value == 0:
        return False
    sum = 0
    for v in str(value):
        sum += int(v) ** len(str(value))
    if sum == value:
        return True
    else:
        return False
def Narcissistic_Numbers(ivalue, fvalue):
    Nar_Num = []
    for i in range(ivalue, fvalue+1):
        if is_Narcissistic_Number(i):
            Nar_Num.append(i)
    return Nar_Num
print(Narcissistic_Numbers(10, 10000))
# Return [153, 370, 371, 407, 1634, 8208, 9474]
