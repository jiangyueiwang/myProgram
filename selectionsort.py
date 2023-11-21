import random
import time
max=100
n=[0]*max
for i in range(max):
    n[i]=random.randint(1,max)
len = len(n)
start=time.time()
for i in range(len-1):
    for j in range(i+1,len):
        if n[i]>n[j]:
            tmp = n[j]
            n[j]=n[i]
            n[i]=tmp
end=time.time()
print(n)
print(end-start)