# lst = [i for i in range(1, 100)]
#
#
# def double(x):
#     return x * 2
#
#
# print(lst)
#
# for i in map(double, lst):
#     print(i)
#

def is_even(x):
    return x % 2 == 0


lst = [i for i in range(100)]
print(list(filter(is_even,lst)))
