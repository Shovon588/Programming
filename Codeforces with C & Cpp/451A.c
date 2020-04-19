#include<stdio.h>
#include<string.h>
int main()
{
	#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	#endif

    int a,b,temp=100;

    scanf("%d%d",&a,&b);
    
    if(a<temp)
    {
    	temp=a;
    }

    if(b<temp)
    {
    	temp=b;
    }

    if(temp%2==0)
    {
    	printf("Malvika\n");
    }
    else
    {
    	printf("Akshat\n");
    }
}