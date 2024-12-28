#include <math.h>
#include <stdio.h>

float somme(int n);

int main(void)
{
    int n;
    printf("donner n: ");
    scanf("%i", &n);
    printf("somme est: %.3f\n", somme(n));
}

float somme(int n)
{
    float sum = 0;
    for (int i = 0; i < n + 1; i++)
    {
        sum += sqrt(i);
    }
    return sum;
}
