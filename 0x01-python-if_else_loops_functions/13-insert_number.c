#include "lists.h"
/**
 * insert_node - that inserts a number into a sorted singly linked list.
 * @head: the head
 * @number: the number to modify
 *
 * Return: new_node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node;
	listint_t *current;

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);

	new_node->n = number;
	new_node->next = NULL;

	if (*head == NULL || (*head)->n >= new_node->n)
	{
		new_node->next = *head;
		*head = new_node;
	}
	else
	{
		current = *head;
		while (current->next != NULL && current->next->n < new_node->n)
		{
			current = current->next;
		}
		new_node->next = current->next;
		current->next = new_node;
	}

	return (new_node);
}
