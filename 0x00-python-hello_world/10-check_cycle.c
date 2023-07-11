#include "lists.h"
/**
 * check_cycle - Entry point
 * Description: check cycle
 * @list: head
 * Return: 1 or 0
 */
int check_cycle(listint_t *list)
{
	int passed = 0;
	listint_t *current;
	listint_t *head = list;

	current = list;
	while (current != NULL)
	{
		if (passed == 0 && current == head)
			passed = 1;
		else if (passed == 1 && current == head)
			return (1);
		current = current->next;
	}
	return (0);
}
