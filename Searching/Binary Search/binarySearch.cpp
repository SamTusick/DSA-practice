// binarySearch.cpp
// Binary Search algorithm using a vector of ints. To use any kind of
// data types just change data type in each function for vector & target

#include <iostream>
#include <vector>

int binarySearch(std::vector<int> array, int target);
int main()
{
    std::vector<int> array = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    int target = 3;
    int result = binarySearch(array, target);

    if (result != -1)
    {
        std::cout << result << "\n";
    }
    else
    {
        std::cout << "No such element\n";
    }
    return 0;
}

int binarySearch(std::vector<int> array, int target)
{
    int low = 0;
    int high = array.size() - 1;

    while (low <= high)
    {
        int mid = (low + high) / 2;

        if (array[mid] == target)
        {
            return mid;
        }

        if (array[mid] > target)
        {
            high = mid - 1;
        }
        else
        {
            low = mid + 1;
        }
    }
    return -1;
}