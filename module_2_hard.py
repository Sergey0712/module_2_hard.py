n = int(input('Введите число ',))
code = ''
for i in range(n):
    if i == 0:
        continue
    for j in range(i + 1, n + 1):
        if (n % (i + j)) == 0:
            code += str(i) + str(j)
print(n, '-', code)