def binary_search(list, find, left, right):
    if right < left:
        return -1

    mid_index = (left + right) // 2
    if mid_index >= len(list) or mid_index < 0:
        return -1

    mid_number = list[mid_index]

    if mid_number == find:
        return mid_index

    if mid_number < find:
        left = mid_index + 1
    else:
        right = mid_index - 1

    return binary_search(list, find, left, right)


if __name__ == '__main__':
    list = [12, 15, 17, 19, 21, 24, 45, 67, 7]
    find = 67

    index = binary_search(list, find, 0, len(list))
    print(f"Ans= {index}")
