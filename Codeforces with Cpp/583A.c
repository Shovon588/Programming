#include<stdio.h>
int main()
{
	#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	#endif

    int n,i,a[255]={0},b[255]={0},v,h,j=0,k[255];
    scanf("%d",&n);

    for(i=0;i<n*n;i++)
    {
    	scanf("%d%d",&v,&h);
    	if(a[v-1]==0 && b[h-1]==0)
    	{
    		k[j]=i+1;
    		a[v-1]++;
    		b[h-1]++;
    		j++;
    	}

    }

    printf("%d",k[0] );
    for(i=1;i<j;i++)
    {
    	printf(" %d",k[i] );
    }
}