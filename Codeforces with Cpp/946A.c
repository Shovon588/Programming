#include<stdio.h>
int main()
{
	#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	#endif

    

    int n,a,pos=0,neg=0,i;

    scanf("%d",&n);

    for(i=0;i<n;i++)
    {
    	scanf("%d",&a);

    	if(a>0)
    	{
    		pos=pos+a;
    	}
    	else if(a<0)
    	{
    		neg=neg+a;
    	}
    }


    printf("%d\n",pos-neg );




}