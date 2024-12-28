#include "helpers.h"
#include <math.h>

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            // calcule average
            int average =
                round((image[i][j].rgbtRed + image[i][j].rgbtGreen + image[i][j].rgbtBlue) / 3.0);
            // changing pixles
            image[i][j].rgbtRed = average;
            image[i][j].rgbtGreen = average;
            image[i][j].rgbtBlue = average;
        }
    }
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width / 2; j++)
        {
            RGBTRIPLE temp = image[i][j];
            image[i][j] = image[i][width - j - 1];
            image[i][width - j - 1] = temp;
        }
    }
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    // making copy
    RGBTRIPLE copy[height][width];
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            copy[i][j] = image[i][j];
        }
    }

    // start calculing average
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            float averageRed = 0, averageBlue = 0, averageGreen = 0, steps = 0;
            for (int y = -1; y < 2; y++)
            {
                if (i + y == -1 || i + y == height)
                    continue;
                for (int x = -1; x < 2; x++)
                {
                    if (j + x == -1 || j + x == width)
                        continue;
                    averageRed += copy[i + y][j + x].rgbtRed;
                    averageGreen += copy[i + y][j + x].rgbtGreen;
                    averageBlue += copy[i + y][j + x].rgbtBlue;
                    steps++;
                }
            }
            image[i][j].rgbtRed = round(averageRed / steps);
            image[i][j].rgbtGreen = round(averageGreen / steps);
            image[i][j].rgbtBlue = round(averageBlue / steps);
        }
    }
    return;
}

// Detect edges
void edges(int height, int width, RGBTRIPLE image[height][width])
{
    // making copy of image
    RGBTRIPLE copy[height][width];
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            copy[i][j] = image[i][j];
        }
    }

    // calcule Gx and Gy
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            float GxR = 0, GyR = 0, GxG = 0, GyG = 0, GxB = 0, GyB = 0;
            for (int y = -1; y < 2; y++)
            {
                for (int x = -1; x < 2; x++)
                {
                    if (i + y == -1 || i + y == height || j + x == -1 || j + x == width)
                        continue;
                    int k = 1;
                    if (x == 0 || y == 0)
                        k = 2;
                    GxR += copy[i + y][j + x].rgbtRed * y * k;
                    GyR += copy[i + y][j + x].rgbtRed * x * k;
                    GxG += copy[i + y][j + x].rgbtGreen * y * k;
                    GyG += copy[i + y][j + x].rgbtGreen * x * k;
                    GxB += copy[i + y][j + x].rgbtBlue * y * k;
                    GyB += copy[i + y][j + x].rgbtBlue * x * k;
                }
            }
            image[i][j].rgbtRed = fmin(255, round(sqrt(pow(GxR, 2) + pow(GyR, 2))));
            image[i][j].rgbtGreen = fmin(255, round(sqrt(pow(GxG, 2) + pow(GyG, 2))));
            image[i][j].rgbtBlue = fmin(255, round(sqrt(pow(GxB, 2) + pow(GyB, 2))));
        }
    }
    return;
}
