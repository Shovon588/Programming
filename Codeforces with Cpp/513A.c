#include<stdio.h>
int main()
{
  #ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
  #endif

    int n1,n2,a,b;
    scanf("%d%d%d%d",&n1,&n2,&a,&b);

    if(n1>n2)
    {
        printf("First\n");
    }
    else
    {
        printf("Second\n");
    }
}
