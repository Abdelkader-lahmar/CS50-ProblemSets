#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>

int main(void)
{
    string phrase = get_string("Text: ");
    int length = strlen(phrase), number_char = 0, number_word = 0, number_sentence = 0;
    for (int i = 0; i < length; i++)
    {
        if (isalpha(phrase[i]))
            number_char++;
        else if (isblank(phrase[i]))
            number_word++;
        else if (phrase[i] == '.' || phrase[i] == '?' || phrase[i] == '!')
            number_sentence++;
    }
    number_word++;
    float L = (float) number_char / number_word * 100;
    float S = (float) number_sentence / number_word * 100;
    float index = 0.0588 * L - 0.296 * S - 15.8;
    if (index < 1)
        printf("Before Grade 1\n");
    else if (index > 16)
        printf("Grade 16+\n");
    else
        printf("Grade %.0f\n", index);
}
