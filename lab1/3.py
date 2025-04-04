n = int(input())
fact = 1
t = []
while n > 0:
    t.append(n)
    fact *= n
    n -=1
print(t)
print(fact)