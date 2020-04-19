#include<stdio.h>
#include<string.h>
int main()
{
	#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	#endif

    int a,b,c,d;
    scanf("%d%d%d%d",&a,&b,&c,&d);

    if(a==c)
    {
    	printf("%d %d %d %d\n",a+d-b,b,c+d-b,d );
    }
    else if(b==d)
    {
    	printf("%d %d %d %d\n",a,b+a-c,c,d+a-c );
    }
    else if(a-c==b-d || a-c==d-b)
    {
    	printf("%d %d %d %d\n",a,d,c,b );
    }
    else
    {
    	printf("-1\n");
    }


}