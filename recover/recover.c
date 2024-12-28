#include <cs50.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

#define JPEG_BLOCK 512

int main(int argc, char *argv[])
{
    // checking command line argumant
    if (argc != 2)
    {
        printf("Usage: ./recover memory.raw");
        return 1;
    }

    // opening memory
    FILE *input = fopen(argv[1], "r");
    if (input == NULL)
    {
        printf("Could not open %s", argv[1]);
        return 1;
    }

    // restoring data
    uint8_t *buffer = malloc(JPEG_BLOCK);
    char *name = malloc(13 * sizeof(uint8_t));
    int i = 0;
    FILE *output = fopen("test.jpg", "r");
    while (fread(buffer, 1, JPEG_BLOCK, input) == JPEG_BLOCK)
    {
        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff &&
            (buffer[3] & 0xef) == 0xe0)
        {
            if (output != NULL) // Ensure there's an open file to close
            {
                fclose(output); // Close the current output file before opening a new one
                output = NULL;  // Set to NULL to avoid potential double close
            }
            sprintf(name, "%03i.jpg", i++);
            output = fopen(name, "w");
            fwrite(buffer, JPEG_BLOCK, 1, output);
        }
        else if (output != NULL)
        {
            fwrite(buffer, JPEG_BLOCK, 1, output);
        }
    }
    fclose(output); // Make sure the last output file is closed
    fclose(input);
    free(buffer);
    free(name);
}
