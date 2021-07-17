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

print(is_Narcissistic_Number(0))
# Return False
print(is_Narcissistic_Number(153))
# Return True
print(is_Narcissistic_Number(115132219018763992565095597973971522401)) # the biggest narcisstic number
# Return True
