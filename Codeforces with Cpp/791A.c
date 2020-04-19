#include<stdio.h>
int main()
{
	#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	#endif

int a,b,count=0;
scanf("%d%d",&a,&b);

while(a<=b)
{
	a=a*3;
	b=b*2;
	count++;
}
printf("%d\n",count );

}