#include "lists.h"
#include <stddef.h>

/**
 * reverse_listint - Reverses a singly-linked listint_t list.
 * @head: A pointer to the starting node of the list to reverse.
 *
 * Return: A pointer to the head of the reversed list.
 */
listint_t *reverse_listint(listint_t **head)
{
    listint_t *current = *head, *next, *prev = NULL;

    while (current)
    {
        next = current->next;
        current->next = prev;
        prev = current;
        current = next;
    }

    *head = prev;
    return *head;
}

/**
 * is_palindrome - Checks if a singly linked list is a palindrome.
 * @head: A pointer to the head of the linked list.
 *
 * Return: If the linked list is not a palindrome - 0.
 *         If the linked list is a palindrome - 1.
 */
int is_palindrome(listint_t **head)
{
    listint_t *current, *reversed, *middle;
    size_t size = 0, i;

    if (*head == NULL || (*head)->next == NULL)
        return 1;

    current = *head;
    while (current)
    {
        size++;
        current = current->next;
    }

    current = *head;
    for (i = 0; i < (size / 2) - 1; i++)
        current = current->next;

    if ((size % 2) == 0 && current->n != current->next->n)
        return 0;

    current = current->next->next;
    reversed = reverse_listint(&current);
    middle = reversed;

    current = *head;
    while (reversed)
    {
        if (current->n != reversed->n)
            return 0;
        current = current->next;
        reversed = reversed->next;
    }

    reverse_listint(&middle);
    return 1;
}
