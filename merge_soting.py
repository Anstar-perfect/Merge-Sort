def merge_sorting(a):
    if len(a)>1:
        mid = len(a)//2
        left = a[:mid]
        right = a[mid:]

        merge_sorting(left)
        merge_sorting(right)

        i=0
        j=0
        k=0

        while i<len(left) and j<len(right):
            if left[i]<=right[j]:
                a[k] = left[i]
                i+=1
            else:
                a[k] = right[j]
                j+=1
            k+=1
        while i<len(left):
            a[k] = left[i]
            i+=1
            k+=1
        while j<len(right):
            a[k] =    right[j]
            j+=1
            k+=1

n = int(input('Enter the number of values:'))
a=[]
for x in range(n):
    value = int(input('Enter the value number '+str(x+1)+' :'))
    a.append(value)
print('Your given array is',a)
merge_sorting(a)
print("Your Sorted Array is",a)    