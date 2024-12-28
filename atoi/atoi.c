#include <cs50.h>
#include <ctype.h>
#include <math.h>
#include <stdio.h>
#include <string.h>

int convert(string input);

int main(void)
{
    string input = get_string("Enter a positive integer: ");

    for (int i = 0, n = strlen(input); i < n; i++)
    {
        if (!isdigit(input[i]))
        {
            printf("Invalid Input!\n");
            return 1;
        }
    }

    // Convert string to int
    printf("%i\n", convert(input));
}

int po = 1;

int convert(string input)
{
    int output = 0, length = strlen(input);
    if (length == 0)
        return 0;
    output += ((int) input[length - 1] - 48) * po;
    po *= 10;
    input[length - 1] = '\0';
    output += convert(input);
    return output;
}
