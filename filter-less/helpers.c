#include "helpers.h"
#include <math.h>

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int average =
                (image[i][j].rgbtRed + image[i][j].rgbtGreen + image[i][j].rgbtBlue + 1.5) / 3.0;
            image[i][j].rgbtRed = average;
            image[i][j].rgbtGreen = average;
            image[i][j].rgbtBlue = average;
        }
    }
    return;
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    /*
    sepiaRed = .393 * originalRed + .769 * originalGreen + .189 * originalBlue
    sepiaGreen = .349 * originalRed + .686 * originalGreen + .168 * originalBlue
    sepiaBlue = .272 * originalRed + .534 * originalGreen + .131 * originalBlue
    */
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            float sepiaRed = 0.393 * image[i][j].rgbtRed + 0.769 * image[i][j].rgbtGreen +
                             0.189 * image[i][j].rgbtBlue;
            if (sepiaRed > 255)
                sepiaRed = 255;
            float sepiaGreen = 0.349 * image[i][j].rgbtRed + 0.686 * image[i][j].rgbtGreen +
                               0.168 * image[i][j].rgbtBlue;
            if (sepiaGreen > 255)
                sepiaGreen = 255;
            float sepiaBlue = 0.272 * image[i][j].rgbtRed + 0.534 * image[i][j].rgbtGreen +
                              0.131 * image[i][j].rgbtBlue;
            if (sepiaBlue > 255)
                sepiaBlue = 255;
            image[i][j].rgbtRed = round(sepiaRed);
            image[i][j].rgbtGreen = round(sepiaGreen);
            image[i][j].rgbtBlue = round(sepiaBlue);
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
    // making copy of image
    RGBTRIPLE copy[height][width];
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            copy[i][j] = image[i][j];
        }
    }
    // start bluring
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            float averageRed = 0, averageGreen = 0, averageBlue = 0;
            int steps = 0;
            for (int k = -1; k < 2; k++)
            {
                for (int kk = -1; kk < 2; kk++)
                {
                    if (i + k < 0 || i + k >= height || j + kk < 0 || j + kk >= width)
                        continue;
                    averageRed += copy[i + k][j + kk].rgbtRed;
                    averageGreen += copy[i + k][j + kk].rgbtGreen;
                    averageBlue += copy[i + k][j + kk].rgbtBlue;
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
