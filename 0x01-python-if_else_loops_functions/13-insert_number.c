#include "lists.h"
#include <stddef.h>
#include <stdlib.h>
/**
 * insert_node - Entry point
 * Description: insert sorted
 * @head: head
 * @number: n
 * Return: nothing
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new = malloc(sizeof(listint_t));
	listint_t *prev;
	listint_t *curr = *head;

	if (new == NULL)
		return (NULL);
	new->n = number;
	if (*head == NULL || *head->n > number)
	{
		new->next = *head;
		*head = new;
		return (new);
	}
	while (curr->n < number && curr->next != NULL)
	{
		prev = curr;
		curr = curr->next;
	}
	if (curr->n < number)
	{
		curr->next = new;
		new->next = NULL;
	}
	else
	{
		new->next = prev->next;
		prev->next = new;
	}
	return (new);
}
