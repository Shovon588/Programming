#include<bits/stdc++.h>
using namespace std;
int main()
{
    int a,b,c,d,one=0,two=0,three=0,four=0,len,i;
    scanf("%d%d%d%d",&a,&b,&c,&d);
    char str[1000005];
    scanf("%s",str);
    len=strlen(str);

    for(i=0;i<len;i++)
    {
        if(str[i]=='1')
        {
            one++;
        }
        else if(str[i]=='2')
        {
            two++;
        }
        else if(str[i]=='3')
        {
            three++;
        }
        else if(str[i]=='4')
        {
            four++;
        }
    }

    one=one*a;
    two=two*b;
    three=three*c;
    four=four*d;

    printf("%d",one+two+three+four);
}
