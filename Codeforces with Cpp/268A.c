#include<stdio.h>
int main()
{
	#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	#endif

int n,i,c,j,count=0;
scanf("%d",&n);
int a[100],b[100];

for(i=0;i<n;i++)
{
scanf("%d%d",&a[i],&b[i]);
}

for(i=0;i<n;i++)
{
for(j=0;j<n;j++)
{
if(a[i]==b[j])
{
count=count+1;
}
}
}


printf("%d",count);


return 0;

}