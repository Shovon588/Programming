#include<stdio.h>
int main()
{
	#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	#endif

int n,a,i,result,j;
scanf("%d",&n);

for(i=0;i<n;i++)
{
	scanf("%d",&a);
	result=1;

	for(j=a;j>0;j--)
	{
		result=result*a;
	}
	printf("%d\n",result );

}


}