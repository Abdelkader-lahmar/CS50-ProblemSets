#include <cs50.h>
#include <stdio.h>

bool prime(int number);

int main(void)
{
    int min, max;
    do
    {
        min = get_int("Minimum: ");
        max = get_int("Maximum: ");
    }
    while (min < 1 || max <= min);

    for (int i = min; i <= max; i++)
    {
        if (prime(i))
        {
            printf("%i\n", i);
        }
    }
}

bool prime(int number)
{
    for (int i = 2; i < number; i++)
    {
        if (number % i == 0)
        {
            return false;
        }
    }
    return true;
}
