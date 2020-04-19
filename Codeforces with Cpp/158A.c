#include<stdio.h>
#include <string.h>
int main()
{
	#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	#endif
	
int n,k,i,b,count=0,c;
scanf("%d%d",&n,&k);
int a[n];

for(i=0;i<n;i++)
{
scanf("%d",&a[i]);
}
b=a[k-1];
c=a[0];

if(c==0){printf("0\n");}
else{
int temp=0;
for(i=0;i<n;i++)
if(a[i]>0)
{
temp=a[i];
if(temp>=b)
{count++;}
}
printf("%d\n",count);
}

}