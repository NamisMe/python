#06-1
def GuGu(n):
    result = []
    i = 1
    while i < 10:
        result.append(n * i)
        i = i + 1
    return result
print(GuGu(3))

#06-2
result = 0
for n in range(1,1000):
    if n % 3 == 0 or n % 5 == 0:
        result += n

print(result)

#06-3
def getTotalPage(m,n):
    if m % n == 0:
        return m // n
    else:
        return m // n + 1

print(getTotalPage(30,10))
print(getTotalPage(40,15))