#Q1
string = "a:b:c:d"
a = string.split(":")
print("#".join(a))

#Q2-1 내 풀이

try:
    a = {'A':90, 'B':80}
    print(a['C'])
except Exception:
    print('70')
#Q2 - ANSWER : get 사용
a = {'A':90, 'B':80}
a.get('C',70) #딕셔너리의 get함수를 사용하면 두 번째 parameter로 전달된 default 값을 대신 돌려준다.

#Q3
a = [1, 2, 3]
print(id(a))

a.extend([4,5]) # extend 사용
print(id(a))

a = [1, 2, 3]
a = a + [4,5] # '+' 사용
print(id(a))
# extend를 사용했을 때는 id가 동일하지만 '+'를 사용했을 때는 id가 달라짐을 볼 수 있음.

#Q4 내 풀이
A = [20, 55, 67, 82, 45, 33, 90, 87, 100, 25]

sum = 0
for i in A:
    if i > 50:
        sum += i
print(sum)

#Q4-ANSWER 
A = [20, 55, 67, 82, 45, 33, 90, 87, 100, 25]

result = 0
while A:                # A 리스트에 값이 있는 동안
    mark = A.pop()      # A리스트의 가장 마지막 항목을 하나씩 뽑아냄
    if mark >= 50:      # 50점 이상의 점수만 더함
        result += mark

print(result)           # 481 출력

#Q5 피보나치 함수 - 내 풀이
def fibonacci(n):
    a = [0,1]
    for i in range(2,n):
        a.append(a[i-1] + a[i-2])
    return a
        
n = input()
print(fibonacci(int(n)))

#Q5 재귀호출 사용
def fib(n):
    if n == 0 : return 0          # n이 0일 때는 0을 반환
    if n == 1 : return 1          # n이 1일 때는 1을 반환
    return fib(n-2) + fib(n-1)    # n이 2 이상일 때는 그 이전의 두 값을 더하여 반환

for i in range(10):
    print(fib(i))
    
#Q6 숫자의 총합 구하기
user_input = input("숫자를 입력하세요.")
numbers = user_input.split(",")
result = 0
for i in numbers:
    result += int(i)

print(result)

#Q7 한 줄 구구단
n = input("숫자를 입력하세요.")
for i in range(1,10):
    print(i * int(n), end = ' ')

# user_input = input("숫자를 입력하세요.")
#n = int(user_input)과 같이 써주면 편리함.

#Q8 
f = open('abc.txt','r')
lines = f.readlines() #모든 라인을 읽음
f.close()

lines.reverse() #역순으로 정렬

f = open('abc.txt','w')
for line in lines:
    line = line.strip() #줄 바꿈문자 제거
    f.write(line)
    f.write('\n') #줄 바꿈 문자 삽입
f.close()
