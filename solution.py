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

# Read input from file 1
with open('input-1.txt', 'r') as f:
    n = int(f.readline())
    arr = list(map(int, f.readline().split()))

# Sort the array
sorted_arr = merge_sort(arr)

# Write output to file 1
with open('output-un.txt', 'w') as f:
    f.write(' '.join(map(str, sorted_arr)))

# Read input from file 2
with open('input-2.txt', 'r') as f:
    n = int(f.readline())
    arr = list(map(int, f.readline().split()))

# Sort the array
sorted_arr = merge_sort(arr)

# Write output to file 2
with open('output-deux.txt', 'w') as f:
    f.write(' '.join(map(str, sorted_arr)))


def compare_files(file1, file2, filenumber):
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        f1_lines = [line.rstrip() for line in f1]
        f2_lines = [line.rstrip() for line in f2]

    max_lines = max(len(f1_lines), len(f2_lines))
    for i in range(max_lines):
        line1 = f1_lines[i] if i < len(f1_lines) else "<no line>"
        line2 = f2_lines[i] if i < len(f2_lines) else "<no line>"
        if line1 != line2:
            print(f"No")
            print(f"Difference at line {i + 1}:")
            print(f"{file1}: {line1}")
            print(f"{file2}: {line2}")
            return
    print("File", filenumber, "Result Matches")

if __name__ == "__main__":
    compare_files('output-1.txt', 'output-un.txt', 1)
    compare_files('output-2.txt', 'output-deux.txt', 2)

