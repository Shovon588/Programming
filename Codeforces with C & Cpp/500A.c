#include<stdio.h>
int main()
{
	#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	#endif

    int n,t,i,temp=1,count=0;
    scanf("%d%d",&n,&t);
    int a;

    for(i=1;i<=n-1;i++)
    {
    	scanf("%d",&a);

        if(i==temp)
        {

    	if((i+a)==t)
    	{
    		count++;
    	}
        else if((i+a)<t)
        {
            temp=i+a;
        }
        else
        {
            temp=0;
        }
    }
}
    
    if(count>0)
    {
    	printf("YES\n");
    }
    else
    {
    	printf("NO\n");
    }
}