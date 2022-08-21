class OrdException(Exception):
    pass


# This should except string.
def ord2(c):
    if len(c) != 1:
        raise OrdException('The function ord2 should except only characters.')
    return ord(c)


# This function should get a number and convert it to ascii_value
def chr2(num):
    if num < 0 or num > 127:
        raise OrdException('This function should get only values between 0<num<127')
    return chr(num)


if __name__ == '__main__':
    num = int(input('Please enter the number to convert to character: '))
    print(chr2(num))

    # Usage of ord2
    c = input('Please enter one character to be converted to ascii.')
    print(ord2(c))
