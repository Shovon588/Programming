#include<stdio.h>
int main()
{
	#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	#endif

    int n,temp,left,count,max;
    scanf("%d",&n);

    temp=n/7;
    left=n%7;
    count=temp*2;

    if(left==6)
    {
    	count=count+1;
    	printf("%d %d\n",count,count+1);
    }

    else
    {

    if(left==1)
    {
    	max=count+1;
    }
    else if(left==2)
    {
    	max=count+2;
    }

    else if(left==0)
    {
    	max=count;
    }
    else if(left>=3)
    {
    	max=count+2;
    }
    printf("%d %d\n",count,max );

}
    

}