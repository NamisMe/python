a = "Life is too short, You need Python"
a[3]

a = "20010331Rainy"
date = a[:8]
weather = a[8:]
print(date)
print(weather)

a="12345678"
print(a[::-2])

a = "I eat %d apples." 

#정렬
print("{0:<10}".format("hi"))
print("{0:>10}".format("hi"))
print("{0:^10}".format("hi"))
print("{0:=^10}".format("hi"))

#f 문자열 포매팅 (파이썬 3.6버전부터 사용가능)

name = '홍길동'
age = 30
print(f'나의 이름은 {name}입니다. 나이는 {age}입니다.')
