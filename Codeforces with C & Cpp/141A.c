#include<stdio.h>
#include<string.h>
int main()
{
	#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	#endif

        char a[100],b[100],c[100];
    int lena,lenb,lenc,suma=0,sumb=0,sumc=0,i;
    scanf("%s%s%s",a,b,c);
    lena=strlen(a);
    lenb=strlen(b);
    lenc=strlen(c);

    for(i=0;i<lena;i++)
    {
      suma=suma+(a[i]-65);
    }

    for(i=0;i<lenb;i++)
    {
      sumb=sumb+(b[i]-65);
    }

    for(i=0;i<lenc;i++)
    {
      sumc=sumc+(c[i]-65);
    }

    if((suma+sumb)==sumc && (suma+sumb)!=2)
    {
      printf("YES\n");
    }
    else
    {
      printf("NO\n");
    }

}