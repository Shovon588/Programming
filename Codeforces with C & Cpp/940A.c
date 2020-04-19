#include<bits/stdc++.h>
using namespace std;
int main()
{
	#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	#endif

    
    int n,d,i,count=0,j,b=0,temp;

    scanf("%d%d",&n,&d);
    int a[n];

    for(i=0;i<n;i++)
    {
    	scanf("%d",&a[i]);
    }


    sort(a,a+n);



    for(i=0;i<n;i++)
    {
    	if(b==1)
    	{
    		break;
    	}
    	else
    	{


    	for(j=n-1;j>0;j--)
    	{
    		temp=a[j]-a[i];
    		
    		if(temp<=d)
    		{
    			b=1;
    			break;
    		}
    		else
    		{
    			count++;
    		}

    		printf("%d--%d\n",temp,count );
    	}
    }

    }

}