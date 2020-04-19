#include<stdio.h>
int main()
{
    int n,i,police=0,count=0;
    scanf("%d",&n);
    int a[n];

    for(i=0;i<n;i++)
    {
        scanf("%d",&a[i]);

        if(a[i]>0)
            {
                police=police+a[i];
        }
        else if(police>0 && a[i]==-1)
        {
            police=police-1;
        }

        else
        {
            count=count+1;
        }
    }
    printf("%d",count);


    return 0;
}
