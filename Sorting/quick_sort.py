# Quick Sort

def quick_sort(arr, low, high):
    if low < high:
        pivot = partition(arr, low, high)
        quick_sort(arr, low, pivot - 1)
        quick_sort(arr, pivot + 1, high) 
    return arr      

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            swap(arr, i, j)

    swap(arr, i + 1, high)
    return i + 1

def swap(arr, i,j):
    arr[i], arr[j] = arr[j], arr[i]

def main():
    sample_array = [112, 64, 34, 25, 12, 22, 11, 32,  90]
    print("Starting Array: ", sample_array)
    sorted_array = quick_sort(sample_array, 0, len(sample_array) - 1)
    print("Sorted array is:", sorted_array)
    return

if __name__ == "__main__":
    main()