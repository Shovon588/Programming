#include<stdio.h>
#include <string.h>
int main()
{
	#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	#endif
	
int n,i,j,sum=0;
scanf("%d",&n);

char str[n][7];
for(i=0;i<n;i++)
{
scanf("%s",str[i]);
}

for(i=0;i<7;i++)
{
int count=0;
for(j=0;j<n;j++)
{
if(str[j][i]=='1')
{
count++;
}
if(count>sum)
{
sum=count;}
}

}
printf("%d\n",sum);


}