// Implements a dictionary's functionality

#include <ctype.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <strings.h>

#include "dictionary.h"

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
} node;

// TODO: Choose number of buckets in hash table
const unsigned int N = 600;

// Hash table
node *table[N];

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    // TODO
    node *temp = table[hash(word)];
    while (temp != NULL)
    {
        if (strcasecmp(temp->word, word) == 0)
        {
            return true;
        }
        else
        {
            temp = temp->next;
        }
    }
    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    // TODO: Improve this hash function
    int num = 0;
    for (int i = 0; word[i] != '\0'; i++)
    {
        num += ((toupper(word[i]) + 5) % 26) * 3.23;
    }
    return num % N;
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    // TODO
    FILE *dic = fopen(dictionary, "r");
    if (dic == NULL)
    {
        return false;
    }
    char word[LENGTH + 1];
    while (fscanf(dic, "%s", word) != EOF)
    {
        int hashed = hash(word);
        node *temp = malloc(sizeof(node));
        if (temp == NULL)
        {
            return false;
        }
        strcpy(temp->word, word);
        temp->next = table[hashed];
        table[hashed] = temp;
    }
    fclose(dic);
    return true;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    // TODO
    int number = 0;
    for (int i = 0; i < N; i++)
    {
        node *temp = table[i];
        while (temp != NULL)
        {
            number++;
            temp = temp->next;
        }
    }
    return number;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    // TODO
    for (int i = 0; i < N; i++)
    {
        while (table[i] != NULL)
        {
            node *temp = table[i]->next;
            free(table[i]);
            table[i] = temp;
        }
    }
    return true;
}
