#include<bits/stdc++.h>
using namespace std;
int main()
{
	#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	#endif

    int t,i,a,b,diff,j,k,count=0;
    char str1[10004],str2[10004],temp;
    scanf("%d",&t);


    for(i=0;i<t;i++)
    {
        count=0;
        scanf("%s",str1);
        scanf("%s",str2);
        a=strlen(str1);
        b=strlen(str2);

        for(j=0;j<a-1;j++)
        {
            if(str1[j]>str1[j+1])
            {
                temp=str1[j];
                str1[j]=str1[j+1];
                str1[j+1]=temp;
            }
        }
        for(j=0;j<b-1;j++)
        {
            if(str2[j]>str2[j+1])
            {
                temp=str2[j];
                str2[j]=str2[j+1];
                str2[j+1]=temp;
            }
        }
        if(b>a)
        {

        for(j=0;j<a;j++)
        {
            for(k=j;k<b;k++)
            {
                if(str1[j]==str2[k])
                {
                    count++;
                    break;
                }
            }
        }
    }
    else
    {
        for(j=0;j<b;j++)
        {
            for(k=j;k<a;k++)
            {
                if(str2[j]==str1[k])
                {
                    count++;
                    break;
                }
            }
        }
    }

        if(a>b)
        {
            diff=a-b;
            count=((b-count)*2)+diff;
        }
        else if(b>a)
        {
            diff=b-a;
            count=((a-count)*2)+diff;
        }
        else
        {
            diff=0;
            count=(a-count)*2;
        }

        

        printf("%d\n",count );

    }


}