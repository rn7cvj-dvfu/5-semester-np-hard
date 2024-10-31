from random import randint, seed

seed(31415926536)

max_val = 6 * 10 ** 11
ranges = [
    (2, 2), (1, 100), (1, 100), (10 ** 2, 10 ** 3), (10 ** 2, 10 ** 3),
    (11 ** 3, 10 ** 4), (10 ** 3, 10 ** 4), (10 ** 4, 10 ** 5), (10 ** 4, 10 ** 5),
    (11 ** 4, 10 ** 5), (10 ** 4, 10 ** 5), (10 ** 5, 10 ** 6), (10 ** 6, 10 ** 7),
    (11 ** 7, 10 ** 8), (10 ** 8, 10 ** 9), (10 ** 9, 10 ** 10), (10 ** 10, 10 ** 11),
    (11 ** 10, 10 ** 11), (max_val, max_val)
]

for index, rand_range in enumerate(ranges):
    open("{}.in".format(str(index + 3).rjust(2, '0')), "w").write(str(randint(*rand_range)))
