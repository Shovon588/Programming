#include<stdio.h>
int main()
{
	#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	#endif


    int n,i,a,sum=0;
    scanf("%d",&n);

    for(i=0;i<n;i++)
    {
    	scanf("%d",&a);

    	if(a==2)
    	{
    		sum=sum+2;
    	}
    	else if(a==1)
    	{
    		sum=sum+1;
    	}
    }


    printf("%d\n",sum/3 );
    


}