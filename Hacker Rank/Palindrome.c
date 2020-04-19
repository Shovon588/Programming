#include<bits/stdc++.h>
using namespace std;
int main()
{
	#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	#endif

    int n,i,j,l,count,k,flag;
    scanf("%d",&n);
    char str[105];

    for(i=0;i<n;i++)
    {
        count=0;
        scanf("%s",str);
        l=strlen(str);

        if(l%2!=0)
        {
            for(j=0,k=l-1;j<l/2,k>l/2;j++,k--)
            {
                if(str[j]==str[k])
                {
                    count++;
                }
                else
                {
                    break;
                }   
            }

            if(count==l/2)
            {
                printf("Yes\n");
            }
            else
            {
                printf("No\n");
            }
        }
        else
        {
            printf("No\n");
        }
    }
}