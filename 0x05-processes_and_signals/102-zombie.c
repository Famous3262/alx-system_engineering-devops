#include "stdio.h"
#include "stdlib.h"
#include "unistd.h"

/**
 * infinite_while - A function that runs forever and returns nothing
 *
 * Return: Always 0
*/
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - A program that creats 5 zombie processes
 *
 * Return: 0 on success
*/
int main(void)
{
	int count = 0;
	pid_t pid;

	while (count < 5)
	{
		pid = fork();
		if (!pid)
			break;
		printf("Zombie process created, PID: %i\n", (int)pid);
		count++;
	}
	if (pid != 0)
		infinite_while();
	return (0);
}
