# Insertion Sort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        j = i 
        while (arr[j] < arr[j - 1] and j > 0):
            temp = arr[j]
            arr[j] = arr[j-1]
            arr[j-1] = temp
            j -= 1
    return arr

def main():
    test_arr = [112, 64, 34, 25, 12, 22, 11, 32, 90]
    sorted_arr = insertion_sort(test_arr)
    print(sorted_arr)

if __name__ == "__main__":
    main()
