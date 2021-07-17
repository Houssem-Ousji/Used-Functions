def Triangular_Numbers(ivalue, fvalue):
    Tri_Num = []
    for i in range(ivalue, fvalue):
        if i == 0:
            pass
        else:
            Tri_Num.append(int((i * (i + 1) / 2)))
    return Tri_Num
print(Triangular_Numbers(0,11))
# Return [1, 3, 6, 10, 15, 21, 28, 36, 45, 55]