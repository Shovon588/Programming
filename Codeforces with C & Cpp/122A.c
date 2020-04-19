#include<stdio.h>
int main()
{
	#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	#endif

    int n;
    scanf("%d",&n);

    if(n%4==0 || n%7==0 || n%47==0 || n%74==0 || n%477==0)
    {
    	printf("YES\n");
    }
    else
    {
    	printf("NO\n");
    }


}