a = [i for i in range(1, 21)]
print(sorted(list(filter(lambda x: x%2 == 0, a))))
t = lambda x: x + 10
print(list(t(x) for x in a))
print(sorted(a, key = lambda x: -x))
