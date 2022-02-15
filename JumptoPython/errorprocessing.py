#try:
    #오류가 발생할 수 있는 구문
#except Exception as e:
    #오류 발생
#else:
    #오류 발생하지 않음
#finally:
    #무조건 마지막에 실행

f = open('foo.txt','w')
try:
    # 무언가를 수행한다.
    data = f.read()
    print(data)
except Exception as e:
    print(e)
finally:
    f.close()
    
for i, name in enumerate(['body','foo','bar']):
    print(i, name)