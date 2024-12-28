// Check that a password has at least one lowercase letter, uppercase letter, number and symbol
// Practice iterating through a string
// Practice using the ctype library

#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>

bool valid(string password);

int main(void)
{
    string password = get_string("Enter your password: ");
    if (valid(password))
    {
        printf("Your password is valid!\n");
    }
    else
    {
        printf("Your password needs at least one uppercase letter, lowercase letter, number and "
               "symbol\n");
    }
}

// TODO: Complete the Boolean function below
bool valid(string password)
{
    bool up = false, low = false, digit = false, pun = false;
    for (int i = 0, length = strlen(password); i < length; i++)
    {
        if (islower(password[i]))
            low = true;
        else if (isupper(password[i]))
            up = true;
        else if (isdigit(password[i]))
            digit = true;
        else if (ispunct(password[i]))
            pun = true;
    }
    if (up && low && digit && pun)
        return true;
    return false;
}
