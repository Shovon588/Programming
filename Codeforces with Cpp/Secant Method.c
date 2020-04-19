#include<bits/stdc++.h>
using namespace std;
int main()
{
	#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	#endif

    int i;
    float a=1,b=2,c=0,fa,fb,temp;

    for(i=0;i<100;i++)
    {
    	fa=(a*a*a)+(3*a)-5;
    	fb=(b*b*b)+(3*b)-5;

    	c=b-((fb*(b-a))/(fb-fa));
    	temp=b-c;
    	if(temp<0)
    	{
    		temp=temp*-1;
    	}

    	printf("a=%.3f	 b=%.3f 	fa=%.3f 	fb=%.3f 	New=%.3f 	Error=%.3f Percent\n",a,b,fa,fb,c,temp*100);
    	if(temp<0.001)
    	{
    		printf("\nSo the Root of the equation is %.3f\n",b );
    		break;
    	}
    	else
    	{
    		a=b;
    		b=c;
    	}
    }
   
}