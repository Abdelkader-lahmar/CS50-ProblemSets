// MY first project "task manager"

// including libreries
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <strings.h>

// constants
#define DEFULT_Task_LIST "tasks_list.csv"
#define MAX_LINE_LENGTH 256

// linked-list deffine
typedef struct node
{
    char name[30];
    char time[6];
    char priority[7];
    char status[6];
    struct node *next;
} node;

// prototype
void create(void);
void load(FILE* task_file);
void delete(void);
void return_task(node* ptr, FILE *file);
int quite(FILE *file);
void display(node *ptr);

//global variables
node* tasks = NULL;

// Main function
int main(int argc, char **argv)
{
    // select Tasks list file
    char *task_list = (argc == 2) ? argv[1] : DEFULT_Task_LIST;

    // open tasks list file
    FILE *task_file = fopen(task_list, "r+");
    if (task_file == NULL)
    {
        printf("can't open %s\n", task_list);
        return 1;
    }

    // home display
    printf("\n\t welcome user to your task manager\n");
    load(task_file);
    while (1)
    {
        printf("--------------------------------------------------------------------------------\n");
        printf("%-20s %-10s %-15s %s\n", "Name", "Time", "Priority", "Status");
        display(tasks);
        printf("--------------------------------------------------------------------------------\n");
        printf("\ncommands: \ncreate: create new task\tdelete: delete old task\t quite: stop the programe\n\nchose: ");
        char *command = malloc(7 * sizeof(char));
        scanf("%s", command);
        if (strcasecmp(command, "create") == 0)
        {
            create();
        }
        else if (strcasecmp(command, "delete") == 0)
        {
            delete();
        }
        else if (strcasecmp(command, "quite") == 0)
        {
            free(command);
            return quite(task_file);
        }
        else
        {
            printf("unknown command!! please enter a valid command\n");
        }
    }
}

// Function to creat tasks
void create(void)
{
    node *temp = malloc(sizeof(node));
    printf("\tcreating new task\n");
    printf("enter name of the task: ");
    scanf("%s", temp->name);
    printf("enter time of the task: ");
    scanf("%s", temp->time);
    printf("chose priority of the task (high/medium/low): ");
    scanf("%s", temp->priority);
    strcpy(temp->status, "still");
    temp->next = tasks;
    tasks = temp;
}

// Function to load tasks
void load(FILE* task_file)
{
    // read file and load tasks
    char *buffer = malloc(MAX_LINE_LENGTH * sizeof(char));
    if (buffer == NULL)
    {
        printf("error happend when loading tasks\n");
    }
    fgets(buffer, MAX_LINE_LENGTH, task_file);
    while(fgets(buffer, MAX_LINE_LENGTH, task_file))
    {
        node *temp = malloc(sizeof(node));
        // load name
        strcpy(temp->name, strtok(buffer, ","));
        // load time
        strcpy(temp->time, strtok(NULL, ","));
        // load priority
        strcpy(temp->priority, strtok(NULL, ","));
        // load status
        strcpy(temp->status, strtok(NULL, "\n"));
        // add new node
        temp->next = tasks;
        tasks = temp;
    }
    free(buffer);
}

// Function to display tasks
void display(node *ptr)
{
    if (ptr == NULL)
        return;
    display(ptr->next);
    printf("%-20s %-10s %-15s %s\n", ptr->name, ptr->time, ptr->priority, ptr->status);
    return;
}

// Function to delete tasks
void delete(void)
{
    printf("\tdeleting old task\ntype name of task: ");
    char temp[30];
    scanf("%s", temp);
    node *current_ptr = tasks, *prev_ptr = current_ptr;
    while (current_ptr != NULL)
    {
        if (strcasecmp(current_ptr->name, temp) == 0)
        {
            prev_ptr->next = current_ptr->next;
            free(current_ptr);
            printf("delete done successfuly\n");
            return;
        }
        prev_ptr = current_ptr;
        current_ptr = current_ptr->next;
    }
    printf("task not found\n");
}

// return tasks to file
void return_task(node* ptr, FILE *file)
{
    if (ptr == NULL)
        return;
    return_task(ptr->next, file);
    fprintf(file, "%s,%s,%s,%s\n", ptr->name, ptr->time, ptr->priority, ptr->status);
    return;
}

int quite(FILE *file)
{
    fseek(file, 0, SEEK_SET);
    fprintf(file, "Tasks,Time,Priority,Status\n");
    return_task(tasks, file);
    while (tasks != NULL)
    {
        node* temp = tasks->next;
        free(tasks);
        tasks = temp;
    }
    fclose(file);
    return 1;
}
