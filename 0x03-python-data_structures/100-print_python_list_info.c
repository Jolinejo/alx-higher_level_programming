#include <stdio.h>
#include "Python.h"

/**
 * print_python_list_info - Entry point
 * @list: list
 * Return: nothing
 */
void print_python_list_info(PyObject *list)
{
	PyListObject *forced;
	int i = 0;

	forced = (PyList Object *)list;
	printf("[*] Size of the Python List = %ld\n", forced->ob_base.ob_size);
	printf("[*] Allocated = %ld\n", forced->allocated);
	for (; i < forced->ob_base.ob_size; i++)
	{
		printf("Element %d: %s\n", forced->ob_item[i]->ob_type->tp_name);
	}
}
