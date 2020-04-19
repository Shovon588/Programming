#include<stdio.h>
int main()
{
	#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	#endif

    int a,b,z,i,tempa,tempb,count=0,j;
    scanf("%d%d%d",&a,&b,&z);

    for(i=1;i<=z;i++)
    {
    	for(j=1;j<=z;j++)
    	{
    		tempa=a*i;
    		tempb=b*j;
    		if(tempa==tempb)
    		{
    			count++;
    			break;
    		}
    	}
    	if((a*i)>=z && (b*i)>=z)
    	{
    		break;
    	}
    }

    	

    printf("%d\n",count );

}