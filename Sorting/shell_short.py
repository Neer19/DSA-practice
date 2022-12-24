def shell_sort(arr):
    size = len(arr)
    gap = size//2

    while gap > 0:
        for i in range(gap,size):
            anchor = arr[i]
            j = i
            while j>=gap and arr[j-gap]>anchor:
                arr[j] = arr[j-gap]
                j -= gap
            arr[j] = anchor
        gap = gap // 2

def foo(arr):
    size = len(arr)
    gap = size // 2
    gap = 3
    for i in range(gap, size):
        anchor = arr[i]
        j = i
        while j>=gap and arr[j-gap]>anchor:
            arr[j] = arr[j-gap]
            j -= gap
        arr[j] = anchor

if __name__ == '__main__':
    test_case = [
        [1,23,56,20,40,8],
        [45,55,36,4,2,1],
        [],
        [89,11,23,87,74,14,23,10]
    ]
    
    for elements in test_case:
        shell_sort(elements)
        print(f'sorted array: {elements}')