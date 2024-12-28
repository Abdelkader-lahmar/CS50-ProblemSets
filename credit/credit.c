#include <cs50.h>
#include <stdio.h>

string check_type(long credit_num);
int isit_valid(long card_num);

int main(void)
{
    long credit_num = get_long("enter your card number ");
    string card_type = check_type(credit_num);
    int last = (isit_valid(credit_num) == 0) ? printf("%s\n", card_type) : printf("INVALID\n");
}

string check_type(long credit_num)
{
    int type = (credit_num / 100000000000000);
    int card = (credit_num / 10000000000000);
    if (type == 51 || type == 52 || type == 53 || type == 54 || type == 55)
        return "MASTERCARD";
    else if (credit_num / 1000000000000000 == 4 || credit_num / 1000000000000 == 4)
        return "VISA";
    else if (card == 34 || card == 37)
        return "AMEX";
    else
        return "INVALID";
}

int isit_valid(long card_num)
{
    int sum = 0;
    for (long i = 10; i <= 1000000000000000; i *= 100)
    {
        int num = ((card_num / i) % 10) * 2;
        sum += ((num % 10) + (num / 10));
    }
    for (long i = 1; i <= 1000000000000000; i *= 100)
    {
        sum += ((card_num / i) % 10);
    }
    return sum % 10;
}
