#include<bits/stdc++.h>
using namespace std;
int main()
{
    int n,m,i,j,c,temp;

    scanf("%d%d",&n,&m);

    char a[n][m];

    scanf("%c",&c);

    for(i=0;i<n;i++)
    {
        for(j=0;j<m;j++)
        {
            scanf("%c",&a[i][j]);
        }
        scanf("%c",&c);
    }


        c=0;

        for(i=0;i<n;i++)
        {
            for(j=0;j<m;j++)
        {
            if(a[i][j]=='*')
            {
                continue;
            }
            else if(a[i][j]=='.')
            {
                if(a[i-1][j]=='*' || a[i+1][j]=='*' || a[i][j-1]=='*' || a[i][j+1]=='*' || a[i-1][j-1]=='*' || a[i-1][j+1]=='*' || a[i+1][j-1]=='*' || a[i+1][j+1]=='*' )
                {
                    c=1;
                    printf("breaking from dot");
                    break;
                }
            }
            else if(a[i][j]>=49 && a[i][j]<=56)
            {
                temp=a[i][j]-'0';

                if(a[i-1][j]=='*')
                {
                    temp--;
                }
                if(a[i+1][j]=='*')
                {
                    temp--;
                }
                if(a[i][j-1]=='*')
                {
                    temp--;
                }
                if(a[i][j+1]=='*')
                {
                    temp=temp-1;
                }
                if(a[i-1][j-1]=='*')
                {
                    temp--;
                }
                if(a[i-1][j+1]=='*')
                {
                    temp--;
                }
                if(a[i+1][j-1]=='*')
                {
                    temp--;
                }
                if(a[i+1][j+1]=='*')
                {
                    temp--;

                }

                if(temp!=0)
                {
                    c=1;
                    printf("breaking from digit\n");
                    printf("%d--%d\n",i,j);
                    break;
                }

            }
        }
        if(c==1)
        {
            break;
        }
    }

   if(i==n && j==m)
   {
       printf("YES");
   }
   else
   {
       printf("NO");

   }



    return 0;
}
