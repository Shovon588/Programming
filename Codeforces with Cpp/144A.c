#include<stdio.h>
int main()
{
	#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	#endif

    int n,i,counta,countb,x=0,y=100,result;
    scanf("%d",&n);
    int a[n];

    for(i=0;i<n;i++)
    {
    	scanf("%d",&a[i]);
    	counta=a[0];
    	countb=a[0];
    }

    for(i=0;i<n;i++)
    {

    	if(a[i]>counta)
    	{
    		if(counta<countb)
    		{
    			countb=counta;
    			y=x;
    		}
    		counta=a[i];
    		x=i;
    	}
    	else if(a[i]<=countb)
    	{
    		countb=a[i];
    		y=i;
    	}
    }






    if(x>y)
    {
    	result=x+(n-y-2);
    }
    else
    {
    	result=x+(n-y-1);
    }

    printf("%d\n",result );


}