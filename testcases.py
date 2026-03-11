'''Edge cases and robustness :
program
testcases**
hidden*
1)understand when they occur
2)categories of the edge classmethod
3)handle the edge case
 
 arrays edge cases:
find the max element in the array DS  
input:
[1,4,2,-1]
abs[-8,-99,1,0,2]
[]=?
[5,5]
[5]'''


#finding max element with many edge(test) cases
'''arr=list(map(int,input("enter elements:").split()))
print(max(arr)) '''

'''error
max() iterable argument is empty
  File "D:\codegnan\dsa\mar10\testcases.py", line 21, in <module>
    print(max(arr))
          ~~~^^^^^
ValueError: max() iterable argument is empty'''

'''arr=list(map(int,input("enter elements:").split()))
if len(arr)==0:
    print("array is empty")
else:
    print(max(arr))'''
#for single lement and duplicate elements
'''arr=list(map(int,input("enter elements:").split()))
if len(arr)==0:
    print("array is empty")
elif len(arr)>1:
    print(max(arr))
else:
    slow=0
    for fast in range(1,len(arr)):
        if arr[slow]!=arr[fast]:
            slow+=1
            arr[slow]=arr[fast]
    print(arr[:slow+1])'''



'''s=input("enter a string:")
s1=" "
print(max(s))
print(max(s1))'''

'''s=input("enter a string:")
if s=="":
    print("string is empty")
else:
    print("length of :",s,"is",len(s))'''


'''space=space
x=palindrome
0==n-1 palindrome

perfect sample->palindrome
space==space
single character==single character(including special characters)
case sensitivity'''
s=input("enter a string:").lower()
if s==s[::-1]:
    print("palindrome")
elif s==" ":
    print("string is empty")
elif len(s)==1:
    print("single character")
elif len(s)<=1:
    print("string is empty")
else:
    print("not a palindrome")




