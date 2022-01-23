Python 3.10.2 (tags/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a="life is too short"
len(a)
17
Life is too short, You need Python
SyntaxError: invalid syntax
a = "Pithon"
a[1]
'i'
a[1] =
SyntaxError: invalid syntax
a[:1]
'P'
[a:2]
SyntaxError: invalid syntax
a[:2]
'Pi'
a[2:]
'thon'
a[:1]+'y'+ a[:2]
'PyPi'
a[:1]+'y
SyntaxError: unterminated string literal (detected at line 1)
a[:1]+'y' + a[2:]
'Python'
"I eat %d apples." % 3
'I eat 3 apples.'
"I eat %s apples." % "five"
'I eat five apples.'
number = 3
"I eat %d apples." % number
'I eat 3 apples.'
number = 10
day = "three"
"I ate %d apples. so I was sick for %s days." % (number, day)
'I ate 10 apples. so I was sick for three days.'
"Error is %d%." % 98
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    "Error is %d%." % 98
ValueError: incomplete format
"Error is %d%%." % 98
'Error is 98%.'
"%10s" % "hi"
'        hi'
"%-10sjane" % 'hi'
'hi        jane'
"%0.4f" % 3.42134234
'3.4213'
"%
SyntaxError: unterminated string literal (detected at line 1)
2.소수점 표현하기
SyntaxError: invalid decimal literal
"I eat {0} apples".format(3)
'I eat 3 apples'
"I eat {0} apples".format("five")
'I eat five apples'
"I ate {number} apples. so I was sick for {day} days.".format(number=10, day=3)
'I ate 10 apples. so I was sick for 3 days.'
"{0:<10}".format("hi")
'hi        '
{0:>10
 
SyntaxError: invalid syntax
"{0:>10}".format("hi
                 
SyntaxError: unterminated string literal (detected at line 1)
"{0:=^10}".format("hi")
                 
'====hi===='
"{0:!<10}".format("hi")
                 
'hi!!!!!!!!'

y = 3.42134234
                 
"{0:0.4f}".format(y)
                 
'3.4213'
"{0:10.4f}".format(y)
                 
'    3.4213'

name = '홍길동'
                 
age = 30
                 
f'나의 이름은 {name}입니다. 나이는 {age}입니다.'
                 
'나의 이름은 홍길동입니다. 나이는 30입니다.'

age = 30
                 
f'나는 내년이면 {age+1}살이 된다.'
                 
'나는 내년이면 31살이 된다.'

d = {'name':'홍길동', 'age'=30}
                 
SyntaxError: ':' expected after dictionary key
d = {'name
     
SyntaxError: unterminated string literal (detected at line 1)
d = {'name':'홍길동', 'age':30}
     
f'나의 이름은 {d["name"]}입니다. 나이는 {d["age"]}입니다.'
     
'나의 이름은 홍길동입니다. 나이는 30입니다.'
