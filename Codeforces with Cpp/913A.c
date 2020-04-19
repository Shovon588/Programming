#include<stdio.h>
#include<math.h>
int main()
{
	#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	#endif

    int n,m,sum;
    scanf("%d%d",&n,&m);
    sum=pow(2,n);

    printf("%d\n",sum );

    printf("%d\n",m%sum );
}