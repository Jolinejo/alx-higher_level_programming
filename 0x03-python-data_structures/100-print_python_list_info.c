#include <stdio.h>
#include <Python.h>
#include <unistd.h>
#include <stdlib.h>
#include "listobject.h"

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
	printf("[*] Size of the Python List = %ld\n",Py_SIZE(forced));
	printf("[*] Allocated = %ld\n", forced->allocated);
	for (; i < Py_SIZE(forced); i++)
	{
		printf("Element %d: %s\n", i, Py_TYPE(forced->ob_item[i])->tp_name);
	}
}
