'''Binary search 
searched in a sorted array
binary search in range

1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
approach:
1.define low=minimum possible answer(range)
2.define high=maximum possible answer(range)
3.take mid
4.check if mid==answer
5.if < -> try all elementsin the left
6.if > -> try all elements in the right'''
#code tom print the evalution of binary search and print the range of search
'''arr=list(map(int,input("enter elements:").split()))
target=int(input("enter target value:"))
low=0
high=len(arr)-1
while low<=high:
    print("searching in range:",low,"to",high)
    mid=(low+high)//2
    if arr[mid]==target:
        print("elment found at :",mid)
        break
    elif arr[mid]<target:
        low=mid+1
    else:
        high=mid-1
if low>high:
    print("ele4ment not found!!!...")'''


'''instead of using sqrt function search function search the answer range and find the square root(floor value )using binary search in range'''

'''n=int(input("enter a number:"))
low=0
high=n
ans=0
while low<=high:
    mid=(low+high)//2
    if mid*mid<n:
        ans=mid
        low=mid+1
    else:
        high=mid-1
print("the square root of",n,"is(floor value):",ans)'''

'''calculate the minimum capacity of a ship for packing weights you have to pack the ship with weights in D-days find the minimum capacity  
weights:[1,2,3,4,5,6,7,8,9 10]
days=5
minimal capacity:15'''
'''w=list(map(int,input("enter weights:").split()))
d=int(input("enter daysw:"))
low=max(w)
high=sum(w)
while low<=high:
    mid=(low+high)//2
    day=1
    capacity=0
    for i in w:
        if capacity+i>mid:
            day+=1
            capacity=0
        capacity+=i
    if day<=d:
        ans=mid
        high=mid-1
    else:
        low=mid+1
print("the minimum capacity of the ship is:",ans)'''


#monkey eating bananas 
#aggressive cows

