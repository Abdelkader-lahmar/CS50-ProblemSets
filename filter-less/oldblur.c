if (i == 0)
            {
                if (j == 0)
                {
                    for (int k = 0; k < 2; k++)
                    {
                        for (int kk = 0; kk < 2; kk++)
                        {
                            averageRed += copy[i + k][j + kk].rgbtRed;
                            averageGreen += copy[i + k][j + kk].rgbtGreen;
                            averageBlue += copy[i + k][j + kk].rgbtBlue;
                        }
                    }
                    image[i][j].rgbtRed = round(averageRed / 4);
                    image[i][j].rgbtGreen = round(averageGreen / 4);
                    image[i][j].rgbtBlue = round(averageBlue / 4);
                }
                else if (j == (width - 1))
                {
                    for (int k = 0; k < 2; k++)
                    {
                        for (int kk = -1; kk < 1; kk++)
                        {
                            averageRed += copy[i + k][j + kk].rgbtRed;
                            averageGreen += copy[i + k][j + kk].rgbtGreen;
                            averageBlue += copy[i + k][j + kk].rgbtBlue;
                        }
                    }
                    image[i][j].rgbtRed = round(averageRed / 4);
                    image[i][j].rgbtGreen = round(averageGreen / 4);
                    image[i][j].rgbtBlue = round(averageBlue / 4);
                }
                else
                {
                    for (int k = 0; k < 2; k++)
                    {
                        for (int kk = -1; kk < 2; kk++)
                        {
                            averageRed += copy[i + k][j + kk].rgbtRed;
                            averageGreen += copy[i + k][j + kk].rgbtGreen;
                            averageBlue += copy[i + k][j + kk].rgbtBlue;
                        }
                    }
                    image[i][j].rgbtRed = round(averageRed / 6);
                    image[i][j].rgbtGreen = round(averageGreen / 6);
                    image[i][j].rgbtBlue = round(averageBlue / 6);
                }
            }
            else if (i == (height - 1))
            {
                if (j == 0)
                {
                    for (int k = -1; k < 1; k++)
                    {
                        for (int kk = 0; kk < 2; kk++)
                        {
                            averageRed += copy[i + k][j + kk].rgbtRed;
                            averageGreen += copy[i + k][j + kk].rgbtGreen;
                            averageBlue += copy[i + k][j + kk].rgbtBlue;
                        }
                    }
                    image[i][j].rgbtRed = round(averageRed / 4);
                    image[i][j].rgbtGreen = round(averageGreen / 4);
                    image[i][j].rgbtBlue = round(averageBlue / 4);
                }
                else if (j == (width - 1))
                {
                    for (int k = -1; k < 1; k++)
                    {
                        for (int kk = -1; kk < 1; kk++)
                        {
                            averageRed += copy[i + k][j + kk].rgbtRed;
                            averageGreen += copy[i + k][j + kk].rgbtGreen;
                            averageBlue += copy[i + k][j + kk].rgbtBlue;
                        }
                    }
                    image[i][j].rgbtRed = round(averageRed / 4);
                    image[i][j].rgbtGreen = round(averageGreen / 4);
                    image[i][j].rgbtBlue = round(averageBlue / 4);
                }
                else
                {
                    for (int k = -1; k < 1; k++)
                    {
                        for (int kk = -1; kk < 2; kk++)
                        {
                            averageRed += copy[i + k][j + kk].rgbtRed;
                            averageGreen += copy[i + k][j + kk].rgbtGreen;
                            averageBlue += copy[i + k][j + kk].rgbtBlue;
                        }
                    }
                    image[i][j].rgbtRed = round(averageRed / 6);
                    image[i][j].rgbtGreen = round(averageGreen / 6);
                    image[i][j].rgbtBlue = round(averageBlue / 6);
                }
            }
            else
            {
                if (j == 0)
                {
                    for (int k = -1; k < 2; k++)
                    {
                        for (int kk = 0; kk < 2; kk++)
                        {
                            averageRed += copy[i + k][j + kk].rgbtRed;
                            averageGreen += copy[i + k][j + kk].rgbtGreen;
                            averageBlue += copy[i + k][j + kk].rgbtBlue;
                        }
                    }
                    image[i][j].rgbtRed = round(averageRed / 6);
                    image[i][j].rgbtGreen = round(averageGreen / 6);
                    image[i][j].rgbtBlue = round(averageBlue / 6);
                }
                else if (j == (width - 1))
                {
                    for (int k = -1; k < 2; k++)
                    {
                        for (int kk = -1; kk < 1; kk++)
                        {
                            averageRed += copy[i + k][j + kk].rgbtRed;
                            averageGreen += copy[i + k][j + kk].rgbtGreen;
                            averageBlue += copy[i + k][j + kk].rgbtBlue;
                        }
                    }
                    image[i][j].rgbtRed = round(averageRed / 6);
                    image[i][j].rgbtGreen = round(averageGreen / 6);
                    image[i][j].rgbtBlue = round(averageBlue / 6);
                }
                else
                {
                    for (int k = -1; k < 2; k++)
                    {
                        for (int kk = -1; kk < 2; kk++)
                        {
                            averageRed += copy[i + k][j + kk].rgbtRed;
                            averageGreen += copy[i + k][j + kk].rgbtGreen;
                            averageBlue += copy[i + k][j + kk].rgbtBlue;
                        }
                    }
                    image[i][j].rgbtRed = round(averageRed / 9);
                    image[i][j].rgbtGreen = round(averageGreen / 9);
                    image[i][j].rgbtBlue = round(averageBlue / 9);
                }
            }
