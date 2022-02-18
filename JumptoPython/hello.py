f = open("C:/Users/CVLAB/NAM/git/python/JumptoPython/import/sample.txt",'r')
lines = f.readlines()
result = 0
for line in lines:
    line = line.strip()
    result += int(line)
    avg = result / len(line)
    print(result,avg)
f.close()