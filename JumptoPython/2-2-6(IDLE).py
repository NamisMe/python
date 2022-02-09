Python 3.10.2 (tags/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#02-6 집합 자료형
s1 = set([1,2,3])
s1
{1, 2, 3}
s2 = set("Hello")
sw2
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    sw2
NameError: name 'sw2' is not defined. Did you mean: 's2'?
s2
{'e', 'H', 'l', 'o'}
s2.sort()
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    s2.sort()
AttributeError: 'set' object has no attribute 'sort'
s1 = set([1,2,3])
l1 = list(s1)
l1
[1, 2, 3]
l1[0]
1
t1 = tuple(s1)
t1
(1, 2, 3)
s1 = set([1,2,3,4,5,6])
s2 = set([4,5,6,7,8,9])

s1 & s2
{4, 5, 6}
{4, 5, 6}
{4, 5, 6}
s1.intersection(s2)
{4, 5, 6}
s1 | s2
{1, 2, 3, 4, 5, 6, 7, 8, 9}
s1.union(s2)
{1, 2, 3, 4, 5, 6, 7, 8, 9}
s2.union(s1)
{1, 2, 3, 4, 5, 6, 7, 8, 9}
s1 - s2
{1, 2, 3}
s2 - s1
{8, 9, 7}
list[s2 - s1]
list[{8, 9, 7}]
list(s2 - s1)
[8, 9, 7]
list(s2 - s1).sort()
list(s2-s1)
[8, 9, 7]
s1 = set([1,2,3])
s1.add(4)
s1
{1, 2, 3, 4}
s1 = set([1,2,3])
s1.update([4,5,6])
s1
{1, 2, 3, 4, 5, 6}
s1.remove(2)
