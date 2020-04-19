#include<bits/stdc++.h>
using namespace std;
int main()
{
	#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	#endif

    int i;
    float a,b,c,fa,foa,temp;

    a=2;

    /*for(i=0;i<100;i++)
    {
    	c=(i*i*i)+(3*i)-5;
    	if(c>0)
    	{
    		break;
    	}
    	else
    	{
    		a=i;
    	}
    }*/


    for(i=0;i<100;i++)
    {
    	fa=(a*a*a)+(3*a)-5;
    	foa=(3*a*a)+3;

    	temp=a-(fa/foa);
    	printf("a=%.3f 		fa=%.3f 	f-a=%.3f 	Xnew=%.3f	diff=%.3f\n",a,fa,foa,temp,a-temp );
    	if(a>temp)
    	{
    		if(a-temp<=0.001)
    		{
    			break;
    		}
    		else
    		{
    			a=temp;
    		}
    	}
    	else
    	{
    		if(temp-a<=0.001)
    		{
    			break;
    		}
    		else
    		{
    			a=temp;
    		}
    	}
    }

   
}