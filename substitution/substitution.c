#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>

bool check_argv(string argv);
string convert(string text, string key);

int main(int argc, string argv[])
{
    if (argc != 2 || check_argv(argv[1]))
    {
        printf("Usage: ./substitution key\n");
        return 1;
    }
    int length = strlen(argv[1]);
    string key = argv[1];
    if (length != 26)
    {
        printf("Key must contain 26 characters.\n");
        return 1;
    }
    else
    {
        for (int i = 0; i < length; i++)
        {
            for (int j = i + 1; j < length; j++)
            {
                if (key[i] == key[j])
                {
                    printf("no dublicte character\n");
                    return 1;
                }
            }
        }
    }
    string text = get_string("plaintext:  ");
    printf("ciphertext: %s\n", convert(text, argv[1]));
}

bool check_argv(string argv)
{
    int length = strlen(argv);
    for (int i = 0; i < length; i++)
    {
        if (!(isalpha(argv[i])))
            return true;
    }
    return false;
}

string convert(string text, string key)
{
    int length = strlen(text), j = 0;
    for (int i = 0; i < length; i++)
    {
        if (isalpha(text[i]))
        {
            if (isupper(text[i]))
            {
                j = text[i] - 65;
                text[i] = toupper(key[j]);
            }
            else
            {
                j = text[i] - 97;
                text[i] = tolower(key[j]);
            }
        }
    }
    return text;
}
