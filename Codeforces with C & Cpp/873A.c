#include<stdio.h>
#include <string.h>
int main()
{
	#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	#endif

int n,k,x,i,initial,j,temp,large=0,result;
scanf("%d%d%d",&n,&k,&x);
int a[n];

initial=k*x;
for(i=0;i<n;i++)
{
scanf("%d",&a[i]);
}
for(i=0;i<n;i++)
{
for(j=i+1;j<n;j++)
{
if(a[i]>a[j])
{
temp=a[i];
a[i]=a[j];
a[j]=temp;
}
}
}

for(i=0;i<n-k;i++)
{
large=large+a[i];
}
result=initial+large;
printf("%d",result);


}