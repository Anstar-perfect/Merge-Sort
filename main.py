def merge_sort(a):
    if len(a)>1:
        mid = len(a)//2
        left = a[:mid]
        right = a[mid:]

        merge_sort(left)
        merge_sort(right)

        i=0
        j=0
        k=0

        while i<len(left) and j<len(right):
            if left[i]<= right[j]:
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
        while j <len(right):
            a[k] = right[j]
            j+=1
            k+=1

a=[23,1,3,34,20,21,32]
print('Unsorted Array',a)
merge_sort(a)
print('Sorted Array {}'.format(a))                                