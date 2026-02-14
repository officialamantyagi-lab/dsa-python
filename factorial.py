import math 
x=int(36)
result=[]
for i in range(1,int(math.sqrt(x))+1):
    if (x%i)==0:
        result.append(i)
        if(x//i!=int(math.sqrt(x))):
            result.append(x//i)
            

print(result)
