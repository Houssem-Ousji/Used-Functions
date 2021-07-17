def is_Prime_Number(value):
    prime = True
    i = 2
    if value in [1, 4]: return False
    while i < value//2 and prime == True:
        if value % i == 0:
            prime = False
        else:
            i += 1
    return prime
def Prime_Numbers(ivalue, fvalue):
    Pri_Num = []
    for i in range(ivalue, fvalue+1):
        if is_Prime_Number(i):
            Pri_Num.append(i)
    return Pri_Num
print(Prime_Numbers(10, 100))
# return [11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
