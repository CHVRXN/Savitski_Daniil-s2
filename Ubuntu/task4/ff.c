#include <unistd.h>
#include <malloc.h>
#include <stdio.h>
#include <sys/mman.h>

int data=10;
int func(int a){
	printf("%i\n", a);
	return func(a+1);
}
int main(int argc, char *argv[])
{
	printf("PID=%i\n", getpid());
	func(1);
	return 0;
}
