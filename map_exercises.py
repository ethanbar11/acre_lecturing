import functools

# Exercise 1

lst = [i * 2 for i in range(10)]
# print(lst)
# print(list(map(lambda x: x ** 2, lst)))
#
# # Exercise 2
#
# print(len(list(filter(lambda x: x % 2 == 0, lst))), len(list(filter(lambda x: x % 2 != 0, lst))))
#
# # Exercise 3
# d = {i: i * 2 for i in range(10)}
# d[50] = 'hello'
# print(dict(filter(lambda t: type(t[1]) != type(''), d.values)))

# Exercise 4
print(functools.reduce(lambda a, b: a + b, lst))
