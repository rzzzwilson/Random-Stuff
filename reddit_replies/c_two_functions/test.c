#include <stdio.h>

typedef void (*fun_ptr)(void);

void alpha(void)
{
    printf("alpha\n");
}

void beta(void)
{
    printf("beta\n");
}

int main(void)
{
    fun_ptr foo;

    foo = alpha;
    foo();
    foo = beta;
    foo();

    return 0;
}
