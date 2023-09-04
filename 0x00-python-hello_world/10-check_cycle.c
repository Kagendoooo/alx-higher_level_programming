#include "lists.h"
/**
 *check_cycle - checks if there is a loop
 *@list: head of list
 *Return: 0 or 1
*/
int check_cycle(listint_t *list)
{
	listint_t *fast = NULL;
	listint_t *slow = NULL;

	if (list == NULL)
		return (0);
	fast = list->next;
	slow = list;
	while (fast && fast->next != NULL)
	{
		if (fast == slow)
			return (1);
		fast = fast->next->next;
		slow = slow->next;
	}
	return (0);
}
