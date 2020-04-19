#include<stdio.h>
int main()
{
	#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	#endif

    int n,i,one,two,three,rem;
    scanf("%d",&n);
    for(i=n+1;i<15000;i++)
    {
    	one=i%10; 
    	rem=i/10;

    	two=rem%10;
    	rem=rem/10;

    	three=rem%10;
    	rem=rem/10;

    	if((one!=two && one!=three && one!=rem) && (two!=one && two!=three && two!=rem) && (three!=one && three!=two && three!=rem) && (rem!=one && rem!=two && rem!=three) )
    	{
    		printf("%d\n",i );
    		break;
    	}

    }



}