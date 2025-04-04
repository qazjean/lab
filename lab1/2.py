n = int(input())
print([i for i in range(1, n+1)])
print([i**2 for i in range(1, n+1)])
s = 0
for i in range(1,n+1):
    s += i
print(s)
