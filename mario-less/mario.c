#include <cs50.h>
#include <stdio.h>

void print_row(int length);
void print_void(int length);

int main(void)
{
    int length;
    do
    {
        length = get_int("how long you want pyramid? ");
    }
    while (!(length > 0));
    for (int i = 0; i < length; i++)
    {
        print_void(length - i - 1);
        print_row(i + 1);
    }
}

void print_row(int length)
{
    for (int i = 0; i < length; i++)
    {
        printf("#");
    }
    printf("\n");
}

void print_void(int length)
{
    for (int i = 0; i < length; i++)
    {
        printf(" ");
    }
}
