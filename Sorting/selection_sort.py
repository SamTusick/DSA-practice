# Selection Sort
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min = i 
        for j in range(i+1, n):
            if arr[j] < arr[min]:
                min = j
        arr[i], arr[min] = arr[min], arr[i]
    return arr

def main():
    arr = [112, 64, 34, 25, 12, 22, 11, 32,  90]
    sorted_arr = selection_sort(arr)
    print("Sorted array:", sorted_arr)

if __name__ == "__main__":
    main()