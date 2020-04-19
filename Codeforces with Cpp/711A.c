#include<stdio.h>
int main()
{
	#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	#endif


    int n,i,count=0,j=0;
    scanf("%d",&n);
    char str[6*n];

    for(i=0;i<6*n;i++)
    {
    	scanf("%c",&str[i]);
    }

    for(i=0;i<6*n;i++)
    {
        if(str[i]=='O' && str[i+1]=='O')
        {
            j=1;
            str[i]='+';
            str[i+1]='+';
            break;
        }
    }

    if(j==0)
    {
        printf("NO\n");
    }
    else
    {
        printf("Yes");
        for(i=0;i<6*n;i++)
        {
            printf("%c",str[i]);
        }
    }



}