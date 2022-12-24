def merge_short(arr):
    if len(arr)<=1:
        return 

    mid=len(arr)//2
    left=arr[mid:]
    right=arr[:mid]

    merge_short(left)
    merge_short(right)

    merge_two(left,right,arr)

def merge_two(a,b,arr):
    sorted_list=[]
    len_a=len(a)
    len_b=len(b)
    i=j=k=0

    while i<len_a and j<len_b:
        if a[i]<=b[j]:
            arr[k]=a[i]
            i+=1
        else:
            arr[k]=b[j]
            j+=1
        k+=1
    while i<len_a:
        arr[k]=a[i]
        i+=1
        k+=1
    while j<len_b:
        arr[k]=b[j]
        j+=1
        k+=1

if __name__ == '__main__':

    test_cases=[
        [1,23,56,20,40,8],
        [45,55,36,4,2,1],
        [],
        [89,11,23,87,74,14,23,10]
    ]
    for arr in test_cases:
        merge_short(arr)
        print(arr)