#include<stdio.h>
#include<string.h>
int main()
{
	#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	#endif

    int n,a,b,temp;
    scanf("%d%d%d",&n,&a,&b);

    temp=n-a;
    if(temp>b)
    {
    	temp=b+1;
    }

    printf("%d\n",temp);

}