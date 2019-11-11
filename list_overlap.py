from random import randint

a = [i for i in range(1, randint(2, 100))]
b = [j for j in range(1, randint(2, 100))]

c = [x for x in a if x in b]
print(c)
