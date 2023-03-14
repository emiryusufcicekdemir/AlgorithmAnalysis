def find_max(arr):
    if len(arr) == 1:
        return arr[0]
    else:
        mid = len(arr) // 2
        left_max = find_max(arr[:mid])
        right_max = find_max(arr[mid:])
        
        return max(left_max, right_max)
