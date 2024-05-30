import random

exploretimes = 100
presenttimes = 10000
deter = 0
result = []
waymax = 1000

e=26.5

for i in range(0,101):
    result.append(0)
totalscore = 0
explore = e
for p in range(0,presenttimes):
    ways = []
    for m in range(0,waymax):
        ways.append(m+1)

    score = 0
    wayvalue = ways.pop(random.randint(0,len(ways)-1))
    score += wayvalue

    for i in range(0,exploretimes-1):
        temp = 0
        deter = random.random()*100
        if explore >= deter:
            if len(ways) !=0:
                temp = ways.pop(random.randint(0,len(ways)-1))
            score += temp
        else:
            score += wayvalue
        
        if wayvalue<= temp:
            wayvalue = temp
    result[round(score/1000)] +=1
    
for i in range(0,20):
    for m in range(0,5):
        print(result[i*5+m],end = ", ")
    print("/")
print(result[100])