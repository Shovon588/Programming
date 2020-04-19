#include<bits/stdc++.h>
using namespace std;
int main()
{

    int n,i;
    char str[1005];
    scanf("%d",&n);


    scanf("%s",str);

    for(i=0;i<n-1;i++)
    {
        if(str[i]=='0' && str[i+1]=='1')
        {
            continue;
        }
        else if(str[i]=='1' && str[i+1]=='0')
        {
            continue;
        }
        else
        {
            break;
        }
    }

    if(n==1 && str[0]=='0')
    {
        printf("No");
    }
    else if(n==1)
    {
        printf("Yes");
    }
    else if(n==2)
    {
        if((str[0]=='0' && str[1]=='0') || (str[0]=='1' && str[1]=='1'))
        {
            printf("No");
        }
        else
        {
            printf("Yes");
        }
    }
    else if(i+1==n)
    {
        printf("Yes");
    }
    else
    {
        printf("No");
    }



    return 0;
}
