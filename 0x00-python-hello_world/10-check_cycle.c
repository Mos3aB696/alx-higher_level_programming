#include "lists.h"
/**
 * check_cycle - function in C that checks if a singly linked list
 * has a cycle in it.
 * @list: the struct
 *
 * Return: 1 if there is a cycle | 0 there is not
 */
int check_cycle(listint_t *list)
{
	listint_t *rabbit, *turtle;

	if (!list)
		return (0);

	rabbit = list;
	turtle = list;

	while (rabbit && rabbit->next)
	{
		turtle = turtle->next;
		rabbit = rabbit->next->next;

		if (turtle == rabbit)
			return (1);
	}
	return (0);
}
