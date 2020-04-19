#include<stdio.h>
int main()
{
	#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	#endif


    int a,b,k,i,j,n=0;
    scanf("%d%d%d",&a,&b,&k);
    char str[a][b],z;

    scanf("%c",&z);
    for(i=0;i<a;i++)
    {
        for(j=0;j<b;j++)
        {
            scanf("%c",&str[i][j]);
        }
        scanf("%c",&z);

    }

    for(i=0;i<a;i++)
    {
        for(j=0;j<b;j++)
        {
            if(str[i][j]=='#')
            {
                printf("#");
            }
            else if(str[i][j]=='.' && str[i+1][j]!='.' && str[i][j-1]!='.')
            {
                if(n<k)
                {
                printf("X");
                n++;
                }
            }
            else if(str[i][j]=='.' && str[i-1][j]!='.' & i!=0 & str[i][j+1]!='.')
            {
                if(n<k)
                {
                    printf("X" );
                    n++;
                }
            }
            else
            {
                printf("%c",str[i][j] );
            }
        }
        printf("\n");
    }
}

