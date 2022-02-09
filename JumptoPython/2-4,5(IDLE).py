Python 3.10.2 (tags/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
t1 = ()
t2 = ()
t2 = (1,)
t3 = (1,2,3)
t4 = 1,2,3
t5 = ('a','b',('ab','cd'))
#튜플의 항목값 변화 불가 -> 값 변하지 않기 원하는 경우 ()의 형태인 튜플 사용해야함
#수시로 값을 변화시켜야 할 경우라면 리스트 [] 사용해야함

튜플의 요소값을 지우거나 변경하려고 하면 어떻게 될까?
SyntaxError: invalid syntax
t1 = (1,2,'a','b')
del t1[0]
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    del t1[0]
TypeError: 'tuple' object doesn't support item deletion
t1[0] = 'c'
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    t1[0] = 'c'
TypeError: 'tuple' object does not support item assignment
t1[1:]
(2, 'a', 'b')
t2 = (3,4)
t1 + t2
(1, 2, 'a', 'b', 3, 4)
t2 = (3,4)
t2 * 3
(3, 4, 3, 4, 3, 4)
(3,4,3,4,3,4)
(3, 4, 3, 4, 3, 4)

#딕셔너리형 자료형
=연관배열(Associative array , Hash)
SyntaxError: invalid syntax
dic = {'name':'pey', 'phone':'0119993323', 'birth': '1118'}'
SyntaxError: unterminated string literal (detected at line 1)
dic = {'name':'pey', 'phone':'0119993323', 'birth': '1118'}
a={1:'a'}
a[2]='b'
a[3]=[1,2,3]
a
{1: 'a', 2: 'b', 3: [1, 2, 3]}
del a[1]
a
{2: 'b', 3: [1, 2, 3]}
{"김연아":"피겨스케이팅", "류현진":"야구", "박지성":"축구", "귀도":"파이썬"}
{'김연아': '피겨스케이팅', '류현진': '야구', '박지성': '축구', '귀도': '파이썬'}

grade = {'pey': 10, 'julliet': 99}
grade['pey']
10
grade[10]
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    grade[10]
KeyError: 10
a = {'a':1,'b':2}
a['a']
1
a['b']
2
a = {(1,2) : 'hi'}
a = {[1,2] " 'hi'}
     
SyntaxError: unterminated string literal (detected at line 1)
a = {[1,2] : 'hi'}
     
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    a = {[1,2] : 'hi'}
TypeError: unhashable type: 'list'
a = {'name': 'pey', 'phone': '0119993323', 'birth': '1118'}
     
a.keys()
     
dict_keys(['name', 'phone', 'birth'])
list(a.keys())
     
['name', 'phone', 'birth']

for k in a.keys():
     print(K)

     
Traceback (most recent call last):
  File "<pyshell#50>", line 2, in <module>
    print(K)
NameError: name 'K' is not defined. Did you mean: 'k'?
for k in a.keys():
     print(k)

     
name
phone
birth

a.items()
     
dict_items([('name', 'pey'), ('phone', '0119993323'), ('birth', '1118')])
a.clear()
     
a
     
{}
a.get('name')
     
a
     
{}
a = {'name':'pey', 'phone':'0119993323', 'birth': '1118'}
     
a.get('name')
     
'pey'
a.get('phone')
     
'0119993323'
a.get('nokey')
     
a['name']
     
'pey'
print(a.get('nokey'))
     
None
a.get('foo','bar')
     
'bar'
a = {'name':'pey','phnoe':'0119993323','birth':'1118'}
     
'name' in a
     
True
'email' in a
     
False
'pey' in a
     
False
