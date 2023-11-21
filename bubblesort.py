import random
import time
max=10000
m =[5,6,7,2,1]
n=[0]*max
for i in range(max):
    n[i]=random.randint(1,10000)
len = len(n)
start=time.time()
for i in range(len-1):
    for j in range(len-i-1):
        if n[j]>n[j+1]:
            tmp = n[j]
            n[j]=n[j+1]
            n[j+1]=tmp
end=time.time()
print(n)
print(end-start)
n1=[0]*max*10
for i in range(max*10):
    n1[i]=random.randint(1,100000)
start=time.time()
n1.sort()
end=time.time()
print(n1)
print(end-start)
