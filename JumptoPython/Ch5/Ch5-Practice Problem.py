#Q1
class Calculator:
    def __init__(self):
        self.value = 0
        
    def add(self, val):
        self.value += val
        
class UpgradeCalculator(Calculator):
    def minus(self,val):
        self.value -= val

cal = UpgradeCalculator()
cal.add(10)
cal.minus(7)

#Q2
class Calculator:
    def __init__(self):
        self.value = 0

    def add(self, val):
        self.value += val

class MaxLimitCalculator(Calculator):
    def __init__(self):
        self.value = 0

    def add(self, val):
        self.value += val
        
        if self.value > 100:
            self.value = 100
        

cal = MaxLimitCalculator()
cal.add(50)
cal.add(60)
cal.add(70)
print(cal.value)

#Q4
def nonnegative(x):
    return x >= 0

print(list(filter(nonnegative,[1,-2,3,-5,8,-3])))
print(list(filter(lambda x: x > 0,[1,-2,3,-5,8,-3])))

#Q5
print(int('0xea',16))

#Q6
def three_times(x):
    return x*3

#Q7
print(list(map(three_times,[1,2,3,4])))
print(list(map(lambda x: x*3,[1,2,3,4])))

#Q8
a = max([-8, 2, 7, 5, -3, 5, 0, 1])
b = min([-8, 2, 7, 5, -3, 5, 0, 1])
print("최댓값은 %d입니다." % a )
print("최댓값은 %d입니다." % b )
print("합은 %s입니다" % str(a+b))
