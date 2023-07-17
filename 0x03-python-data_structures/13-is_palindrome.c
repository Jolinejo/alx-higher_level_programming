#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome - check the code for
 * @head: head
 * Return: Always 0.
 */
int is_palindrome(listint_t **head)
{
	int len = 0;
	int i, j;
	listint_t *curr;
	listint_t *nex;

	if (*head == NULL || (*head)->next == NULL)
		return (1);
	curr = *head;
	nex = curr;
	while (nex->next != NULL)
	{
		nex = nex->next;
		len++;
	}
	len++;
	if (nex->n != curr->n)
		return (0);
	for (i = 1; i < len / 2; i++)
	{
		curr = curr->next;
		nex = curr;
		for (j = i; j < len - i - 1; j++)
			nex = nex->next;
		if (nex->n != curr->n)
			return (0);
	}
	return (1);

}
