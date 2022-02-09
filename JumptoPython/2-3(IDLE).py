Python 3.10.2 (tags/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

a = [1,2,3]

a
[1, 2, 3]
a[-1]
3
a = [1, 2, 3, ['a', 'b', 'c']]
a[0]
1
a[-1]
['a', 'b', 'c']
a[3][1]
'b'
a = [1, 2, ['a', 'b', ['Life', 'is']]]
a[2][2][0]
'Life'
a = [1,2,3,4,5]
a[0:2]
[1, 2]
a=
SyntaxError: invalid syntax
a="12345"
a[0:2]
'12'
a = [1, 2, 3, ['a', 'b', 'c'], 4, 5]
a[3][:-1]
['a', 'b']
a[3][:-2]
['a']
a = [1,2,3]
a * 3
[1, 2, 3, 1, 2, 3, 1, 2, 3]
len(a)
3
str(a[2])+"hi"
'3hi'
a = [1,2,3]
a[2] = 4
a
[1, 2, 4]
del a[1]
a
[1, 4]
a=[1,2,3,4,5]
del a[2:]
a
[1, 2]
a = [1,2,3]
a.append(4)
A
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    A
NameError: name 'A' is not defined. Did you mean: 'a'?
A
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    A
NameError: name 'A' is not defined. Did you mean: 'a'?
a
[1, 2, 3, 4]
a = [1,4,3,2]
a.sort()
a
[1, 2, 3, 4]
a=['a
   
SyntaxError: unterminated string literal (detected at line 1)
a=['a','b','c']
   
a.sort()
   
a
   
['a', 'b', 'c']
a = ['a','c','b']
   
a.reverse
   
<built-in method reverse of list object at 0x000001EACD9E59C0>
a
   
['a', 'c', 'b']
a.reverse()
   
a
   
['b', 'c', 'a']
a = [1,2,3]
   
a.index(3)
   
2
a.index(1)
   
0
a.index(0)
   
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    a.index(0)
ValueError: 0 is not in list
a = [1,2,3]
   
a.insert(0,4)
   
a
   
[4, 1, 2, 3]
a.remove(3)
   
a
   
[4, 1, 2]
a = [1,2,3,1,2,3]
   
a.remove(3)
   
a
   
[1, 2, 1, 2, 3]
a.remove(2)
   
a
   
[1, 1, 2, 3]
a = [a,1,2,b,c,3,d,4,a,1,b]
   
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    a = [a,1,2,b,c,3,d,4,a,1,b]
NameError: name 'b' is not defined
a =
   
SyntaxError: invalid syntax
a = ['a',1,2,'b',1,5,3,'c',2,1]
   
a.remove(3)
   
a
   
['a', 1, 2, 'b', 1, 5, 'c', 2, 1]
a.remove('a')
   
a
   
[1, 2, 'b', 1, 5, 'c', 2, 1]

a=[1,2,3]
   
a.pop()
   
3
a
   
[1, 2]
a=['a',1,2,'b',1,5,3,'c',2,1]
   
a.pop(3)
   
'b'
a
   
['a', 1, 2, 1, 5, 3, 'c', 2, 1]
a.append(3,'b')
   
Traceback (most recent call last):
  File "<pyshell#81>", line 1, in <module>
    a.append(3,'b')
TypeError: list.append() takes exactly one argument (2 given)
a.append('b',3)
   
Traceback (most recent call last):
  File "<pyshell#82>", line 1, in <module>
    a.append('b',3)
TypeError: list.append() takes exactly one argument (2 given)
a.append('b')
   
a
   
['a', 1, 2, 1, 5, 3, 'c', 2, 1, 'b']
a.sort
   
<built-in method sort of list object at 0x000001EACD9E6100>
a.sort()
   
Traceback (most recent call last):
  File "<pyshell#86>", line 1, in <module>
    a.sort()
TypeError: '<' not supported between instances of 'int' and 'str'
str(a)
   
"['a', 1, 2, 1, 5, 3, 'c', 2, 1, 'b']"
a.sort()
   
Traceback (most recent call last):
  File "<pyshell#88>", line 1, in <module>
    a.sort()
TypeError: '<' not supported between instances of 'int' and 'str'
a = [1,2,3]
   
a.extend([4,5])
   
a
   
[1, 2, 3, 4, 5]
b = [6,7]
   
a.extend(b)
   
a
   
[1, 2, 3, 4, 5, 6, 7]
a.extend([4,5])
   
a.extend(['a','b'])
   
a
   
[1, 2, 3, 4, 5, 6, 7, 4, 5, 'a', 'b']
