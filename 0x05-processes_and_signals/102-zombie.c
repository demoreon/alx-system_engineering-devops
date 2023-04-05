#include <unistd.h>
#include <stdlib.h>
#include <stdio.h>

/**
 * infinite_while
 * Return: 0
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
 * main - create zombie processes
 * Return: infinite_while
 */
int main(void)
{
	pid_t zombie;
	unsigned int i;

	for (i = 0; i < 5; i++)
	{
		zombie = fork();
		if (zombie == 0)
			exit(0);
		else
			printf("Zombie process created, PID: %d\n", zombie);
	}
	return (infinite_while());
}
