def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    # Merge the two sorted arrays
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    # Append any remaining elements
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Read input from file
with open('input-1.txt', 'r') as f:
    n = int(f.readline())
    arr = list(map(int, f.readline().split()))

# Sort the array
sorted_arr = merge_sort(arr)

# Write output to file
with open('output.txt', 'w') as f:
    f.write(' '.join(map(str, sorted_arr)))
