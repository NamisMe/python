Python 3.10.2 (tags/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a = 1
b = "python"
c = [1,2,3]

a = [1,2,3]
id(a)
1757843575808
a = [1,2,3]
b = a
id(b)
1757875202176
id(a)
1757875202176
a is b
True
a[1] = 4
b
[1, 4, 3]
a =[1,2,3]
b = a[:]
a[1]=4
a
[1, 4, 3]
b
[1, 2, 3]
from copy import copy
a = [1,2,3]
b = copy(a)
b = copy(a)
b is a
False
b = a.copy()
b
[1, 2, 3]
b is a
False
a, b = ('python','life')
(a, b) = 'python','life'
[a,b] = 'python','life'
[a,b] = ['python','life']
a = b = ['python']
a = 3
b = 5
a, b = b,a
a
5
b
3
