#advanced hashing
'''mixed approaches to solve a problem  very effecctively than sigle approach
2 sum
1 2 4 6 10
l        r 
l+=1
r-=1
t=14
4 sum
a+b+c+d=t#here the sum of 3 independent and non repeated values
arr=1 0 -1 0 -2 2
t=0
sorted=[-2,-1,0,0,1,2]
possible output of quadruplets
[-2,0,0,2]
[-2,-1,1,2]
[-1,0,0,1]

Approach by hashing with two pointer 
1)original array converted to a sorted array
[1,0,-1,0,-2,2]
sorted=[-2,-1,0,0,1,2]
2)first element =i
  second element=j    
3)left-j+1
  right=n-1
4)sum=arr[i]+arr[j]+arr[left]+arr[right]
5)sum<t:      left+=1
  sum<t:      right-=1
  sum==t:     store target
Time complexity:O(n^3)'''

#code to find all unique quadruplets in any given array for the target value using hash+2 pointer+ sort
'''arr=list(map(int,input("enter the array:").split()))
target=int(input("enter target:"))
arr.sort()
n=len(arr)
res=[]
for i in range(n-3):
    if i>0 and arr[i]==arr[i-1]:#to avoid duplicates
        continue
    for j in range(i+1,n-2):
        if j>i+1 and arr[j]==arr[j-1]:#to avoid duplicates
            continue
        left=j+1
        right=n-1
        while left<right:
            sum=arr[i]+arr[j]+arr[left]+arr[right]
            if sum==target:
                res.append([arr[i],arr[j],arr[left],arr[right]])
                left+=1
                right-=1
                while left<right and arr[left]==arr[left-1]:#to avoid duplicates
                    left+=1
                while left<right and arr[right]==arr[right+1]:#to avoid duplicates
                    right-=1
            elif sum<target:
                left+=1
            else:
                right-=1
for q in res:
    print(q)'''



