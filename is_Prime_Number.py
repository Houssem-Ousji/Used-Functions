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
print(is_Prime_Number(1))
#You got : False
print(is_Prime_Number(5))
#You got : True
print(is_Prime_Number(7877))
#You got : True


