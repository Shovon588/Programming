#include<stdio.h>
int main()
{
	#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	#endif


    int n,m,count=0,sum=0,i,temp;

    scanf("%d%d",&n,&m);

    temp=n;
    if(n<m)
    {
        printf("-1\n");
    }
    else
    {
    for(i=n;i>=0;i--)
    {
        if(i%2==0)
        {
            count=temp-i;
            if(((i/2)+count)%m==0)
            {
                 printf("%d\n",(i/2)+count );
                 break;
            }
        }
        else if(i<=0)
        {
            printf("-1\n");
        }
    }
}


}