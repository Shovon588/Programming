#include<stdio.h>
int main()
{
	#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	#endif

   int n,i,count=0,b,j;
   scanf("%d",&n);
   char a[n];

   scanf("%d",&b);
   for(i=0;i<n;i++)
   {
   		scanf("%c%d",&a[i],&b);
   } 

   for(i=0;i<n;i++)
   {
   		if(a[i]=='f')
   		{
   			if(i==0)
   			{
   				for(j=1;j<n;j++)
   				{
   					if(a[j]=='f')
   					{
   						continue;
   					}
   					else
   					{
   						break;
   					}
   				}
   			}
   			count++;
   			break;
   		}
   }

   for(i=j;i<n;i++)
   {
   		if(a[i]=='f' && a[i+1]!='f' && a[i+1]=='s')
   		{
   			count++;
   		}
   }

   printf("%d\n",count%1000000007 );

}