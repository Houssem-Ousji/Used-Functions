def is_Perfect_Number(value):
    dividers = 0
    for i in range(1, (value//2)+1):
        if value % i == 0:
            dividers += i
    if dividers == value:
        return True
    else:
        return False
print(is_Perfect_Number(1))
#You got : False
print(is_Perfect_Number(6))
#You got : True
print(is_Perfect_Number(8128))
#You got : True


