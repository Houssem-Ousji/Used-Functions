def is_Perfect_Number(value):
    dividers = 0
    for i in range(1, (value//2)+1):
        if value % i == 0:
            dividers += i
    if dividers == value:
        return True
    else:
        return False
def Perfect_Numbers(ivalue, fvalue):
    Per_Num = []
    for i in range(ivalue, fvalue+1):
        if is_Perfect_Number(i):
            Per_Num.append(i)
    return Per_Num
print(Perfect_Numbers(10, 2000))
# return  [28, 496]