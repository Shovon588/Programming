#include<stdio.h>
#include <string.h>
int main()
{
	#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	#endif

int n,i,go,come,total=0,j,temp;
scanf("%d",&n);
int a[n];
for(i=0;i<n;i++)
{
scanf("%d%d",&go,&come);
total=total-go+come;
a[i]=total;
}
for(i=0;i<n;i++)
{
for(j=i+1;j<n;j++)
{
if(a[i]<a[j])
{
temp=a[i];
a[i]=a[j];
a[j]=temp;
}
}
}
printf("%d",a[0]);


}