Python 3.10.1 (tags/v3.10.1:2cd268a, Dec  6 2021, 19:10:37) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
pocket = ['paper','money','cellphone']
if 'money' in pocket: pass
else: print("카드를 꺼내라")

ㄹ
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    ㄹ
NameError: name 'ᄅ' is not defined
d
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    d
NameError: name 'd' is not defined. Did you mean: 'id'?
if score >= 60:

    message = "success:
    
SyntaxError: unterminated string literal (detected at line 3)
if score >= 60:
    message = "success"
else:
    message = "failure"
score = 70
SyntaxError: invalid syntax
message
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    message
NameError: name 'message' is not defined

================================ RESTART: Shell ================================
treeHit = 0
while treeHit < 10:
    treeHit = treeHit +1
    print("나무를 %d번 찍었습니다." % treeHit)
    if treeHit == 10:
        print("나무 넘어갑니다.")

        
나무를 1번 찍었습니다.
나무를 2번 찍었습니다.
나무를 3번 찍었습니다.
나무를 4번 찍었습니다.
나무를 5번 찍었습니다.
나무를 6번 찍었습니다.
나무를 7번 찍었습니다.
나무를 8번 찍었습니다.
나무를 9번 찍었습니다.
나무를 10번 찍었습니다.
나무 넘어갑니다.
prompt = """
1. Add
2. Del
3. List
4. Quit

Enter number: """

number = 0
while number != 4:
    print(prompt)
    number = int(input())

    

1. Add
2. Del
3. List
4. Quit

Enter number: 
4
1
1
coffee = 10
money = 300
while money:
    print("돈을 받았으니 커피를 줍니다.")
    coffee = coffee - 1
    print("남은 커피의 양은 %d개입니다." % coffee)
    if coffee == 0:
        print("커피가 다 떨어졌습니다. 판매를 중지합니다.")
        break

    
돈을 받았으니 커피를 줍니다.
남은 커피의 양은 9개입니다.
돈을 받았으니 커피를 줍니다.
남은 커피의 양은 8개입니다.
돈을 받았으니 커피를 줍니다.
남은 커피의 양은 7개입니다.
돈을 받았으니 커피를 줍니다.
남은 커피의 양은 6개입니다.
돈을 받았으니 커피를 줍니다.
남은 커피의 양은 5개입니다.
돈을 받았으니 커피를 줍니다.
남은 커피의 양은 4개입니다.
돈을 받았으니 커피를 줍니다.
남은 커피의 양은 3개입니다.
돈을 받았으니 커피를 줍니다.
남은 커피의 양은 2개입니다.
돈을 받았으니 커피를 줍니다.
남은 커피의 양은 1개입니다.
돈을 받았으니 커피를 줍니다.
남은 커피의 양은 0개입니다.
커피가 다 떨어졌습니다. 판매를 중지합니다.
