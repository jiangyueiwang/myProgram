n=[0,1,2,3,4,5,6,7,8,9]
key = 0
len = len(n)
found = False
lower = 0
upper = len-1
mid = (lower+upper) // 2 
while (key != n[mid] and lower<=upper):
    if key > n[mid]:
        lower=mid + 1
    else:
        upper = mid-1
    mid = (lower+upper)//2
if lower > upper :
    print("Not found")
else:
    print(mid)