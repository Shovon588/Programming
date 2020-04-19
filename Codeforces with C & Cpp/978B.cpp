#include<bits/stdc++.h>
using namespace std;
int main()
{
    char str[105];
    int n,i,count=0;

    scanf("%d%s",&n,str);

    for(i=0;i<n-2;i++)
    {
        if(str[i]=='x' && str[i+1]=='x' && str[i+2]=='x')
        {
            count++;
        }
    }

    printf("%d",count);

 return 0;
}
