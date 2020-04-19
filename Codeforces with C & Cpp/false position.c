#include<bits/stdc++.h>
using namespace std;
int main()
{
	#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	#endif

    float a=1,b=2,fa,fb,c,d;
    int i;

    for(i=0;i<100;i++)
    {
    	fa=(a*a*a)+(3*a)-5;
    	fb=(b*b*b)+(3*b)-5;

    	c=((a*fb)-(b*fa))/(fb-fa);
    	d=(c*c*c)+(3*c)-5;

    	if(d>0)
    	{
    		if(c-b<=0.001)
    		{
    			break;
    		}
    		else
    		{
    			b=c;
    		}
    	}
    	else if(d<0)
    	{
    		if(c-a<=0.001)
    		{
    			break;
    		}
    		else
    		{
    			a=c;
    		}
    	}



    	printf("a=%.3f	b=%.3f	fa=%.3f 	fb=%.3f 	c=%.3f 	fc=%.3f\n",a,b,fa,fb,c,d);
    }

}