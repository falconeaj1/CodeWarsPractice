def add_binary(a,b):
    print('adding ', a, '+', b)
    x = a+b
    largestPower = 0
    negative = False
    if x < 0:
        x = -x
        negative = True

    if not(x==(x%1)):
        x -= (x%1)
    if x == 0:
        return '0'
    while (x-2**largestPower >= 0):
        largestPower += 1
    largestPower -= 1
    print('largest power = ', largestPower, '=', 2**largestPower)
    digitString = ''
    for digit in range(largestPower+1):
        if (x - 2**(largestPower-digit)) >= 0:
            x -= 2**(largestPower-digit)
            digitString += '1'
        else:
            digitString += '0'
    if negative:
        digitString = '-'+digitString
    print(digitString)
    return digitString
# print(add_binary(-3.9,0))
print(hex(781514))