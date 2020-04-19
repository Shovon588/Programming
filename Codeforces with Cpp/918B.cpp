#include<bits/stdc++.h>
using namespace std;
int main()
{
    int n,m,l,size,j,i,k;
    scanf("%d%d",&n,&m);
    int a[n];
    char ip[100],name[n][100],command[100];

    for(i=0;i<n;i++)
    {
        size=0;
        scanf("%s %s",name[i],ip);
        l=strlen(ip);
        for(j=0;j<l;j++)
        {
            size=size+ip[j];
        }
        a[i]=size;
    }

    for(i=0;i<m;i++)
    {
        size=0;
        scanf("%s %s",command,ip);
        l=strlen(ip);
        for(j=0;j<l-1;j++)
        {
            size=size+ip[j];
        }
        for(k=0;k<n;k++)
        {
            if(size==a[k])
            {
                printf("%s %s #%s\n",command,ip,name[k]);
                break;
            }
        }
    }



    return 0;
}
