
            int valur[3] = {1 , 2 , 1};
            int kk = 0;
            for (int y = -1; y < 2; y++)
            {
                int k = 0;
                if (i + y == -1 || i + y == height)
                {
                    kk++;
                    continue;
                }
                for (int x = -1; x < 2; x++)
                {
                    if (j + x == -1 || j + x == width)
                    {
                        k++;
                    }
                    GxR += copy[i + y][j + x].rgbtRed * y * valur[k];
                    GyR += copy[i + y][j + x].rgbtRed * x * valur[kk];
                    GxG += copy[i + y][j + x].rgbtGreen * y * valur[k];
                    GyG += copy[i + y][j + x].rgbtGreen * x * valur[kk];
                    GxB += copy[i + y][j + x].rgbtBlue * y * valur[k];
                    GyB += copy[i + y][j + x].rgbtBlue * x * valur[kk];
                    k++;
                }
                kk++;
            }
            image[i][j].rgbtRed = round(sqrt(pow(GxR, 2) + pow(GyR, 2)));
            image[i][j].rgbtGreen = round(sqrt(pow(GxG, 2) + pow(GyG, 2)));
            image[i][j].rgbtBlue = round(sqrt(pow(GxB, 2) + pow(GyB, 2)));
