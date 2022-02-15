
    
def positive(l):
    result = []
    for i in l:
        if i > 0:
            result.append(i)
    return result
    
print(positive([1,-3,2,0,-5,6]))

def negative(x):
    return x <= 0

a = list(filter(negative, [1, -3, 2, 0, -5, 6]))
print(a)

#two_times.py
def two_times(numberList):
    result = []
    for number in numberList:
        result.append(number*2)
    return result

result = two_times([1,2,3,4])
print(result)

#two_times2.py
def two_times2(x):
    return x*2

a = list(map(two_times2, [1, 2, 3, 4]))
print (a)

b = list(map(lambda a: a*2, [1,2,3,4]))
print (b)