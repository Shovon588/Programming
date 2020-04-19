#include<stdio.h>
#include<string.h>
int main()
{
    int n,i,Ant=0,Dan=0;
    scanf("%d",&n);
    char str[n];
    scanf("%s",str);
    for(i=0;i<n;i++)
    {
        if(str[i]=='A')
        {
            Ant++;
        }
        else
        {
            Dan++;
        }
    }

    if(Ant>Dan)
    {
        printf("Anton");
    }
    else if(Dan>Ant)
    {
        printf("Danik");
    }
    else
    {
        printf("Friendship");
    }

    return 0;
}


