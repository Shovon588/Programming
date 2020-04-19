#include<stdio.h>
int main()
{
	#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	#endif

    
    int n,i,sum=0,totalkg=0,j;
    scanf("%d",&n);
    int kg[n],tk[n];

    for(i=0;i<n;i++)
    {
    	scanf("%d%d",&kg[i],&tk[i]);
    }


    for(i=0;i<n;i++)
    {
        for(j=i;j<n;j++)
        {
                if(tk[i]<=tk[j])
                {
                    totalkg=totalkg+(tk[i]*kg[j]);
                }

                else
                {
                    totalkg=totalkg+(tk[j]*kg[j]);
                    i=j;
                }
     
        }
       
        if(j>=n-1 || i>=n-1)
        {
            break;
        }
    }


printf("%d\n",totalkg );

}