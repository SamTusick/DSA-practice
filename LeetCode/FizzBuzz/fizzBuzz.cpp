// FizzBuzz.cpp
#include <string>
#include <vector>

class Solution
{
public:
    std::vector<std::string> fizzbuzz(int n)
    {
        std::vector<std::string> answer;

        for (int i = 0; i <= n; i++)
        {
            bool fizz = i % 3 == 0;
            bool buzz = i % 5 == 0;

            if (fizz && buzz)
            {
                answer.push_back("FizzBuzz");
            }
            else if (fizz)
            {
                answer.push_back("Fizz");
            }
            else if (buzz)
            {
                answer.push_back("Buzz");
            }
            else
            {
                answer.push_back(std::to_string(i));
            }
        }
        return answer;
    }
};

int main()
{
    Solution mySolution(int num = 15);
}