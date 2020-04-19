#include<stdio.h>
#include<string.h>
int main()
{
	#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	#endif

    int n,i,left=0,right=0;
    scanf("%d",&n);
    long long int a[n],b[n];

    for(i=0;i<n;i++)
    {
        scanf("%lld%lld",&a[i],&b[i]);

        if(a[i]<0 && b[i]>0)
        {
            left++;
        }
        else if(a[i]<0 && b[i]<0)
        {
            left++;
        }
        else if(a[i]>0 && b[i]>0)
        {
            right++;
        }
        else if(a[i]>0 && b[i]<0)
        {
            right++;
        }
    }

    if((left==0 || left==1) && (right>=left))
    {
        printf("YES\n");
    }
    else if((right==0 || right==1) && (left>=right))
    {
        printf("YES\n");
    }
    else
    {
        printf("NO\n");
    }

}