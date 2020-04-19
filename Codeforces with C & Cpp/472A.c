#include<stdio.h>
int main()
{
	#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	#endif

    int n,i;
    scanf("%d",&n);

    if(n%2==0)
    {
    	printf("4 %d\n",n-4 );
    }
    else
    {
    	printf("9 %d\n",n-9 );
    }

   }