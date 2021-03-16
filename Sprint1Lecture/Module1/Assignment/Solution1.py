# Sprint 1, Module Project 1

"""
csAlphanumericRestriction
Just go through each character and count how many letters, numbers,
and other types of character the string has. Perform the proper checks at the end.

def csAlphanumericRestriction(input_str):
    numLetters = 0
    numNumbers = 0
    numOther = 0
    for char in input_str:
        if char.isdigit():
            numNumbers += 1
        elif char.isalpha():
            numLetters += 1
        else:
            numOther += 1
    if numOther > 0:
        return False
    return (numNumbers > 0 and numLetters == 0) or (numLetters > 0 and numNumbers == 0)


csOppositeReverse
Iterate through the string in reverse and append the opposite case
to your resulting string.

def csOppositeReverse(txt):
    res = ""
    for i in reversed(range(len(txt))):
        if txt[i].isupper():
            res += txt[i].lower()
        else:
            res += txt[i].upper()
    return res


csSquareAllDigits
You could have done some clever math tricks for this one. An option to make it
simpler is to cast the number to a string so you can easily get each digit.
You can just convert the string back to a number in the end.

def csSquareAllDigits(n):
    numberStr = str(n)
    resStr = ""
    for digit in numberStr:
        resStr += str(int(digit) ** 2)
    return int(resStr)

"""