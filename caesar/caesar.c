#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

bool check(string argv);
string convert(string text, int k);

int main(int argc, string argv[])
{
    if (argc != 2 || check(argv[1]))
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }
    int k = atoi(argv[1]) % 26;
    string text = get_string("plaintext:  ");
    printf("ciphertext: %s\n", convert(text, k));
}

bool check(string argv)
{
    for (int i = 0, length = strlen(argv); i < length; i++)
    {
        if (!(isdigit(argv[i])))
        {
            return true;
        }
    }
    return false;
}

string convert(string text, int k)
{
    int length = strlen(text);
    for (int i = 0; i < length; i++)
    {
        if (isalpha(text[i]))
        {
            if (isupper(text[i]))
            {
                if (text[i] + k > 90)
                    text[i] = text[i] + k - 26;
                else
                    text[i] += k;
            }
            else
            {
                if (text[i] + k > 122)
                    text[i] = text[i] + k - 26;
                else
                    text[i] += k;
            }
        }
    }
    return text;
}
