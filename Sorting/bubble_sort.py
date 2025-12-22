# Bubble Sort

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        j += 1
    i += 1
    return arr

def main():
    sample_array = [112, 64, 34, 25, 12, 22, 11, 32,  90]
    sorted_array = bubble_sort(sample_array)
    print("Sorted array is:", sorted_array)

if __name__ == "__main__":
    main()