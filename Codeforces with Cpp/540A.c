#include<stdio.h>
#include<string.h>
int main()
{
    int n,i,a,c,d,count=0;
    scanf("%d",&n);
    char str1[n],str2[n];
    scanf("%s%s",str1,str2);

    for(i=0;i<n;i++)
    {
       if(str1[i]>str2[i])
       {
           c=str1[i]-str2[i];
           d=10-str1[i]+str2[i];

           if(c<d)
           {
               count=count+c;
           }
           else{count=count+d;}
       }
       else if(str1[i]<str2[i])
       {
           c=str2[i]-str1[i];
           d=10-str2[i]+str1[i];

           if(c<d){count=count+c;}
           else{count=count+d;}
       }
    }

    printf("%d",count);

    return 0;
}
