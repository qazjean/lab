a = [int(input()) for i in range(3)]
print(max(a))
print(min(a))
print("Числа равные" if a[1]==a[0]==a[2] else "Числа неравные")