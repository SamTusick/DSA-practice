# Merge Sort
# Divide and Conquer 

# Divide the array in half until each is only 1 element
# Conquer to sort
# Merge sorted arrays together

def merge_sort(arr):
    # Dividing the array
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) //  2
    left = arr[:mid]
    right = arr[mid:]
    print(left, right)

    sorted_left = merge_sort(left)
    sorted_right = merge_sort(right)
    return merge(sorted_left, sorted_right)

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result

def main():
    sample_array = [112, 64, 34, 25, 12, 22, 11, 32,  90]
    print("Starting Array: ", sample_array)
    sorted_array = merge_sort(sample_array)
    print("Sorted array is:", sorted_array)

if __name__ == "__main__":
    main()