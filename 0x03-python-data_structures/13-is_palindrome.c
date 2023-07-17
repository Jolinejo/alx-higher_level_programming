#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * check - check the code for
 * @head: head
 * @len: len
 * Return: Always 0.
 */
int check(const int len, listint_t **head)
{
	int numbers[2000];
	int i = 0;
	listint_t *curr = *head;

	for (; i < len; i++)
	{
		numbers[i] = curr->n;
		curr = curr->next;
	}
	for (i = 0; i < len / 2; i++)
	{
		if (numbers[i] != numbers[len - i - 1])
			return (0);
	}
	return (1);
}

/**
 * is_palindrome - check the code for
 * @head: head
 * Return: Always 0.
 */
int is_palindrome(listint_t **head)
{
	int len = 0;
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
	return (check(len, head));
}
