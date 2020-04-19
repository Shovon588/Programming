#include<bits/stdc++.h>
using namespace std;
int main()
{
    int n,k,i,tempa,tempb,m=0,j;
    scanf("%d%d",&n,&k);
    int a[n],b[n];

    for(i=0;i<n;i++)
    {
    	scanf("%d",&a[i]);
    	b[i]=i+1;
    }

    for(i=0;i<n;i++)
    {
    	for(j=i+1;j<n;j++)
    	{
    	    if(a[i]>a[j])
            {
                tempa=a[i];
                tempb=b[i];
                a[i]=a[j];
                b[i]=b[j];
                a[j]=tempa;
                b[j]=tempb;
            }
    	}
    }

    for(i=0;i<n && k>=a[i];i++)
    {
        k=k-a[i];
        m++;
    }
    printf("%d\n",m);
    for(i=1;i<=m;i++)
    {
        printf("%d ",b[i-1]);
    }

}
