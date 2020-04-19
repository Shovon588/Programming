#include<stdio.h>
int main()
{
	#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	#endif

    int n,i,result=1,a;
    scanf("%d",&n);

    for(i=0;i<n;i++)
    {
    	scanf("%d",&a);
    	if(a==1)
    	{
    		result=-1;
    		break;
    	}
    }

    printf("%d\n",result );

}