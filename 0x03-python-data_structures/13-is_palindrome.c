#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * reverse - reverses a linked list
 * @head: double pointer to head node
 * Return: pointer to first node of reversed list
 */
listint_t *reverse(listint_t **head)
{
	listint_t *prev = NULL;
	listint_t *current = *head;
	listint_t *next;
	while (current != NULL)
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
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: double pointer to head node
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head, *fast = *head, *second_half, *prev_slow = *head;
	if (*head != NULL && (*head)->next != NULL)
	{
		while (fast != NULL && fast->next != NULL)
		{
			fast = fast->next->next;
			prev_slow = slow;
			slow = slow->next;
		}
		if (fast != NULL)
		{
			slow = slow->next;
		}
		second_half = slow;
		prev_slow->next = NULL;
		reverse(&second_half);
		while (*head && second_half)
		{
			if ((*head)->n == second_half->n)
			{
				*head = (*head)->next;
				second_half = second_half->next;
			}
			else
				return 0;
		}
	}
	return 1;
}
