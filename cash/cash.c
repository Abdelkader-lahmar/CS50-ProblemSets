#include <cs50.h>
#include <stdio.h>

int quarters(int *change);
int dimes(int *change);
int nickels(int *change);
int pennies(int *change);

int main(void)
{
    int change;
    do
    {
        change = get_int("change owed: ");
    }
    while (!(change >= 0));
    int i = quarters(&change);
    i += dimes(&change);
    i += nickels(&change);
    i += pennies(&change);
    printf("%i\n", i);
}

int quarters(int *change)
{
    int i = 0;
    while (*change >= 25)
    {
        *change -= 25;
        i++;
    }
    return i;
}

int dimes(int *change)
{
    int i = 0;
    while (*change >= 10)
    {
        *change -= 10;
        i++;
    }
    return i;
}

int nickels(int *change)
{
    int i = 0;
    while (*change >= 5)
    {
        *change -= 5;
        i++;
    }
    return i;
}

int pennies(int *change)
{
    int i = 0;
    while (*change > 0)
    {
        *change -= 1;
        i++;
    }
    return i;
}
