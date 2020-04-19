#include<stdio.h>
int main()
{
	#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	#endif

    int n,i,p1=1,p2=2,check=3,temp,count=0;
    scanf("%d",&n);
    int a[n];

    for(i=0;i<n;i++)
    {
    	scanf("%d",&a[i]);
    }
    
    for(i=0;i<n;i++)
    {
    	if(a[i]==p1)
    	{
    		temp=p2;
    		p2=check;
    		check=temp;
    		p1=a[i];
    	}
    	else if(a[i]==p2)
    	{
    		temp=p1;
    		p1=a[i];
    		p2=check;
    		check=temp;
    	}
    	else
    	{
    		break;
    	}
 		
    }

   if(n==i)
   {
   	printf("YES\n");
   }
   else
   {
   	printf("NO\n");
   }



}