#include<bits/stdc++.h>
using namespace std;
int main()
{
	#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	#endif

    int i;
    float a,b,c,fa,fb,fc;

    a=0;

    for(i=0;i<100;i++)
    {
    	c=(i*i*i)+(3*i)-5;
    	if(c>0)
    	{
    		b=i;
    		break;
    	}
    	else
    	{
    		a=i;
    	}
    }

    for(i=0;i<100;i++)
    {
    	fa=(a*a*a)+(3*a)-5;
    	fb=(b*b*b)+(3*b)-5;

    	c=(a+b)/2;
    	fc=(c*c*c)+(3*c)-5;

    	if(fc>0)
    	{
    		if(b-a<=0.001)
    		{
    			printf("Congratulations You have done the Bisection Method !\n");
    			break;
    		}
    		else
    		{
    			b=c;
    		}
    	}
    	else if(fc<0)
    	{
    		if(b-a<=0.001)
    		{
    			printf("\nCongratulations You have done the Bisection Method !\n");
    			break;
    		}
    		else
    		{
    			a=c;
    		}
    	}
    	printf("a=%.3f 	b=%.3f 	fa=%.3f 	fb=%.3f 	c=%.3f 	fc=%.3f 	dif=%.3f\n",a,b,fa,fb,c,fc,b-a );

    }

    

}