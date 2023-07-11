#include "lists.h"
/**
 * check_cycle - Entry point
 * Description: check cycle
 * @list: head
 * Return: 1 or 0
 */
int check_cycle(listint_t *list)
{
	listint_t *normal = list;
	listint_t *skip = list;

	while (skip != NULL && skip->next != NULL)
	{
		if (skip == normal)
			return (1);
		normal = normal->next;
		skip = skip->next->next;
	}
	return (0);
}
