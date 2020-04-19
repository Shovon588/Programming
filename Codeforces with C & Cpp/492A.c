#include<stdio.h>
int main()
{
	#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	#endif

int i=1,j=2,n,count=1,temp=1;
scanf("%d",&n);

while(n-temp>=i+j)
{
i=i+j;
j=j+1;
temp=temp+i;
count++;
}

printf("%d\n",count);


}