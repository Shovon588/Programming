#include<bits/stdc++.h>
using namespace std;
int main()
{
	#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	#endif


    long long int a[14],i,even=0,odd=0,temp=0,temp_i;

    for(i=0;i<14;i++)
    {
    	scanf("%lld",&a[i]);

    	if(a[i]!=0 && a[i]%2==0)
    	{
    		even++;
    	}
    	else
    	{
    		odd++;
    	}

    	if(a[i]>temp)
    	{
    		temp=a[i];
    		temp_i=i;
    	}
    }


    long long int total=0;


    if(even>odd)
    {
    	for(i=0;i<14;i++)
    	{
    		if(a[i]%2==0)
    		{
    			total=total+a[i];
    		}
    	}
    }
    else
    {
    	for(i=temp_i+1;i<14;i++)
   		{
   			if(temp>0)
   			{
   				a[i]=a[i]+1;
   				temp=temp-1;

   				if(i==13)
   				{
   					i=0;
   				}
   			}
   			else
   			{
   				break;
   			}


    	}

    }

    for(i=0;i<14;i++)
    {
    	if(a[i]%2==0)
      {
        total=total+a[i];
      }
    }

    printf("%lld\n",total );

}