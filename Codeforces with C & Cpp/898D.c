#include<stdio.h>
int main()
{
	#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	#endif


    int n,i,temp,j,m,k;
    scanf("%d%d%d",&n,&m,&k);
    int a[n];

    for(i=0;i<n;i++)
    {
    	scanf("%d",&a[i]);
    }

    for(i=0;i<n;i++)
    {
    	for(j=0;j<n;j++)
    	{
    		if(a[i]<a[j]){
    		temp=a[i];
    		a[i]=a[j];
    		a[j]=temp;
    	}
    	}
    }

    temp=a[0];


}