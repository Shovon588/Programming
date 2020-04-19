#include<bits/stdc++.h>
using namespace std;
int main()
{

    char str[105];
    int n,i,j,count=0,check=0;
    char temp[2];

    scanf("%d%s",&n,str);

    temp[0]=str[0];
    temp[1]=str[1];

    for(i=0;i<n-1;i++)
    {
        count=1;
        for(j=i+1;j<n;j++)
        {
            if(str[i]==str[j] && str[i+1]==str[j+1])
            {
                count++;
                if(count>check)
                {
                    check=count;
                    temp[0]=str[i];
                    temp[1]=str[i+1];
                }
            }

        }
    }
    printf("%c%c",temp[0],temp[1]);




    return 0;
}
