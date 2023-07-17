#include <stdio.h>
#include <Python.h>
#include <unistd.h>
#include <stdlib.h>

/**
 * print_python_list_info - Entry point
 * @list: list
 * Return: nothing
 */
void print_python_list_info(PyObject *list)
{
	PyListObject *forced;
	int i = 0;

	forced = (PyListObject *)list;
	printf("[*] Size of the Python List = %d\n", forced->ob_base.ob_size);
	printf("[*] Allocated = %d\n", forced->allocated);
	for (; i < forced->ob_base.ob_size; i++)
	{
		printf("Element %d: %s\n", i, forced->ob_item[i]->ob_type->tp_name);
	}
}
