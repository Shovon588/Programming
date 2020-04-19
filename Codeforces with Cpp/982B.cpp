#include<bits/stdc++.h>
using namespace std;

int main()
{
    int n,i,j,len,temp1,temp2,k;

    scanf("%d",&n);
    int a[n],b[n],temp[2*n];
    char str[2*n];

    for(i=0;i<n;i++)
    {
        scanf("%d",&a[i]);
        b[i]=i+1;
    }


    for(i=0;i<n-1;i++)
    {
        for(j=i+1;j<n;j++)
        {
            if(a[i]>a[j])
            {
                temp1=a[i];
                a[i]=a[j];
                a[j]=temp1;

                temp2=b[i];
                b[i]=b[j];
                b[j]=temp2;
            }
        }
    }

    scanf("%s",str);

    len=strlen(str);

    j=0;
    k=0;
    for(i=0;i<len;i++)
    {
        if(str[i]=='0')
        {
            printf("%d ",b[j]);
            temp[k]=b[j];
            j++;
            k++;
        }
        else
        {
            printf("%d ",temp[k-1]);
            k--;
        }
    }





    return 0;
}
