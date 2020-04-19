#include<bits/stdc++.h>
using namespace std;
int main()
{
    long long int n,i,m=100005,len,kuro,shiro,katie;
    int temp;

    char str1[m],str2[m],str3[m];

    scanf("%lld",&n);

    scanf("%s%s%s",str1,str2,str3);


    len=strlen(str1);

    printf("%lld\n",len);

    int arr1[100]={0};
    for(i=0;i<len;i++)
    {
        temp=str1[i]-'A';
        arr1[temp]++;
    }
    sort(arr1,arr1+100);
    kuro=arr1[99]+n;
    printf("%d\n",arr1[99]);


    int arr2[100]={0};
    for(i=0;i<len;i++)
    {
        temp=str2[i]-'A';
        arr2[temp]++;
    }

    sort(arr2,arr2+100);

    shiro=arr2[99]+n;
    printf("%d\n",arr2[99]);


    int arr3[100]={0};

    for(i=0;i<len;i++)
    {
        temp=str3[i]-'A';
        arr3[temp]++;
    }

    sort(arr3,arr3+100);

    katie=arr3[99]+n;
    printf("%d\n",arr3[99]);


    if(kuro>len)
    {
        temp=kuro-len;
        kuro=len-temp;
    }
    if(shiro>len)
    {
        temp=shiro-len;
        shiro=len-temp;
    }

    if(katie>len)
    {
        temp=katie-len;
        katie=len-temp;
    }



    if(kuro>shiro && kuro>katie)
    {
        printf("Kuro");
    }
    else if(shiro>kuro && shiro>katie)
    {
        printf("Shiro");
    }
    else if(katie>kuro && katie>shiro)
    {
        printf("Katie");
    }
    else if(kuro==shiro && shiro==katie)
    {
        printf("Draw");
    }





    return 0;
}
