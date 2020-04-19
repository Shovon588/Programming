#include<bits/stdc++.h>
using namespace std;
int main()
{
    int n,t,i,j,check=1,big=0;
    scanf("%d",&t);
    int a[t];

    for(i=0;i<t;i++)
    {
        scanf("%d",&a[i]);

        if(a[i]==big)
        {
            check++;
        }
        else if(a[i]>big)
        {
            big=a[i];
            check=1;
        }
    }

    if(check%2==0)
    {
        printf("Agasa");
    }
    else
    {
        printf("Conan");
    }

}
