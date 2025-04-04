import random
a = [random.randint(1, 101) for i in range(20)]
print(list(filter(lambda x: x%2 == 0, a)))
print(list(filter(lambda x: x%3 == 0, a)))
print(sum(a)/len(a))