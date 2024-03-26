def solution(arr):
    #convert arr to set to remove dup
    arr2=set(arr)
    
    #convert set to list
    arr1=[i for i in arr2]
    arr1.sort()

    #check if all elements are negative
    if arr1[-1]<=0: 
        print(1)
        return

    for i in range(len(arr1)-1):
        if arr1[i]+1 ==0:
            continue
        if arr1[i]+1 !=arr1[i+1]:
            print(arr1[i]+1)
            return
    print(arr1[-1]+1)

#time complexity = O(n)
#space complexity = O(n)


##############################
    r
#[2,1,4,3,2,1,1,4] l=2 r=4 [2,3,4] count=3
 l       

#min=4   
#seen={4,3,2} count=0
def solution1(a,l,r):
    left,right=0,0
    setty={i for i in range(l,r+1)}
    seen=set()
    scount=len(setty)
    mini= float("inf")
    out=[]

    while right <len(a):
        if a[right] in setty and a[right] not in seen:
            seen.add(a[right])
            scount-=1
    
        if scount==0:
            mini=min(mini,right-left+1)
            print(a[left:right+1])
            while scount<1:
                if a[left] in setty and a[left] in seen:     
                    seen.remove(a[left])
                    scount+=1
                    print("innnnnn")
                left+=1

        right+=1
    
    print(mini)

def shortest_subarray_with_range(a, l, r):
    setty = set(range(l, r + 1))
    seen = set()
    min_length = float('inf')
    left = 0

    for right in range(len(a)):
        if a[right] in setty:
            seen.add(a[right])

        while seen.issuperset(setty):
            min_length = min(min_length, right - left + 1)
            if a[left] in setty:
                seen.remove(a[left])
            left += 1

    return min_length if min_length != float('inf') else -1

# Test the function
#print(shortest_subarray_with_range([2, 1, 4, 3, 2, 1, 1, 4], 2, 4))  # Output: 3



##########################
def solution2(s,c):  
    mapp={}
    count=0
    counter1=0
    for index,letter in enumerate(s):
        if letter not in mapp:
            mapp[letter]=[index]
        else:
            mapp[letter].append(index)

    for i in c:
        for lst in mapp.values():
            if len(lst)>=2:  
                if i>lst[0] and i<=lst[1]:
                    #expect error
                    counter1+=1
                    count+=1
                    lst.pop(0)
        count-=counter1
        counter1=0

    for i in mapp.values():
        if len(i)>=2:
            print(-1)
            return
    print(count)
            

        
            
solution2('aabcba',[1,3,2])