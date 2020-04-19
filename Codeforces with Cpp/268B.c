#include<stdio.h>
int main()
{
	#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	#endif

    int n,i,fail=0,total;

    scanf("%d",&n);
    for(i=1;i<=n;i++)
    {
    	fail=fail+(n-i)*i;
    }

    total=fail+n;

    printf("%d\n",total );

}