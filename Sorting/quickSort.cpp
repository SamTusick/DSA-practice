#include <iostream>
#include <vector>

void swap(int &a , int &b);
int partition(std::vector<int>& list_vector, int low, int high);
void quickSort(std::vector<int>& list_vector, int low, int high);
void printVector(const std::vector<int>& vec); //used for testing

int main()
{
    std:: vector<int> myList = {2,8,9,10,12,3,5,7,6,4,1};

    std::cout << "Original List: "; //used for testing
    printVector(myList); //used for testing

    quickSort(myList, 0, myList.size() - 1);

    std::cout << "Sorted List: "; //used for testing
    printVector(myList); //used for testing


    return 0;
}

void swap(int &a , int &b)
{
    int temp = a;
    a = b;
    b = temp;
}

int partition(std::vector<int>& list_vector, int low, int high)
{
    //Set pivot to end, j to start, and i to j - 1
    int pivot = list_vector[high];
    int i = low;

    //Compare j to pivot
    //Go until j reaches pivot
    //when j > pivot -> j++
    for(int j = low; j < high; j++)
    {
        //when j < pivot -> swap and i++
       if(list_vector[j] <= pivot)
        {
           //then swap i and j
           swap(list_vector[i],list_vector[j]);
           i++;
        }
    }

    //then swap i+ 1 and pivot
    swap(list_vector[i], list_vector[high]);
    //return i
    return i;
}

void quickSort(std::vector<int>& list_vector, int low, int high)
{
    if( low < high )
    {
        int pivotIndex = partition(list_vector, low, high);
        quickSort(list_vector, low, pivotIndex - 1);
        quickSort(list_vector, pivotIndex + 1, high);
    }
}

void printVector(const std::vector<int>& vec) { //used for testing
    for (size_t i = 0; i < vec.size(); ++i) {
        std::cout << vec[i] << " ";
    }
    std::cout << std::endl;
}

