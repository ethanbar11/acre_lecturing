# print(5/0)
try:
    lst = []
    print(lst[5])
    print(5 / 0)
except ZeroDivisionError:
    print('We handled the zero division error.')
except IndexError:
    print('You tried to use the wrong index.')
except:
    print('This will work for all exceptions.')


