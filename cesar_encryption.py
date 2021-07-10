def cesar_encryption(text, direction,value):
    text_2 = ''
    if direction != 'R' and direction != 'L':
        return print("Invalid Direction(R:Right // L:Left)")
    while value > 26:
        value = value - 26
    for i in text:
        if direction == 'R':
            shift = ord(i) + value
            if i.isupper():
                if shift > 90:
                    shift = shift - 90 - 1
                    text_2 += (chr(65 + shift))
                else:
                    text_2 += chr(shift)
            elif i.islower():
                if shift > 122:
                    shift = shift - 122 - 1
                    text_2 += (chr(97 + shift))
                else:
                    text_2 += chr(shift)
            else:
                text_2 += i
        elif direction == 'L':
            shift = ord(i) - value
            if i.isupper():
                if shift < 65:
                    shift = 65 - shift - 1
                    text_2 += (chr(90 - shift))
                else:
                    text_2 += chr(shift)
            elif i.islower():
                if shift < 97:
                    shift = 97 - shift - 1
                    text_2 += (chr(122 - shift))
                else:
                    text_2 += chr(shift)
            else:
                text_2 += i
    return (text_2)

print(cesar_encryption('Hello World !', 'R', 5))
# You got : Mjqqt Btwqi !
print(cesar_encryption('Hello World !', 'L', 5))
# You got : Czggj Rjmgy !