def Triangular_Number(n):
    return int((n*(n+1) / 2))
def is_Triangular_Number(value):
    if value == 0:
        return False
    i = 1
    while value >= Triangular_Number(i):

        if value == Triangular_Number(i):
            return True
        i += 1
    return False
print(is_Triangular_Number(55))
# Return True
print(is_Triangular_Number(150))
# Return False