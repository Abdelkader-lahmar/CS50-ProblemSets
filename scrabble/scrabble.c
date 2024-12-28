#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>

int calcule_points(string player);

int main(void)
{
    string player1 = get_string("player1: ");
    string player2 = get_string("player2: ");
    int score_p1 = calcule_points(player1);
    int score_p2 = calcule_points(player2);
    if (score_p1 > score_p2)
        printf("Player 1 wins!\n");
    else if (score_p2 > score_p1)
        printf("Player 2 wins!\n");
    else
        printf("Tie!\n");
}

int calcule_points(string player)
{
    int score = 0;
    for (int i = 0, length = strlen(player); i < length; i++)
    {
        player[i] = toupper(player[i]);
        if (player[i] == 'A' || player[i] == 'E' || player[i] == 'I' || player[i] == 'L' ||
            player[i] == 'N' || player[i] == 'O' || player[i] == 'R' || player[i] == 'S' ||
            player[i] == 'T' || player[i] == 'U')
            score++;
        else if (player[i] == 'D' || player[i] == 'G')
            score += 2;
        else if (player[i] == 'B' || player[i] == 'C' || player[i] == 'M' || player[i] == 'P')
            score += 3;
        else if (player[i] == 'F' || player[i] == 'H' || player[i] == 'V' || player[i] == 'W' ||
                 player[i] == 'y')
            score += 4;
        else if (player[i] == 'K')
            score += 5;
        else if (player[i] == 'J' || player[i] == 'X')
            score += 8;
        else if (player[i] == 'Q' || player[i] == 'Z')
            score += 10;
    }
    return score;
}
