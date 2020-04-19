#include<bits/stdc++.h>
using namespace std;
int main()
{
	#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	#endif

    int a[6],i,count=1,one=1,big=0;

    for(i=0;i<6;i++)
    {
    	scanf("%d",&a[i]);
    }


    sort(a,a+6);




    for(i=0;i<5;i++)
    {
        if(a[i]==a[i+1])
        {
            one++;
            continue;
        }
        else
        {
            if(one>big)
            {
                big=one;
            }
            one=1;
            count++;
        }
    }
    if(one>big)
    {
        big=one;
    }


    if((count==3 && big>=4) || (count==2 && big==5))
    {
        printf("Bear\n");
    }
    else if((count==2 && big==4) || count==1)
    {
        printf("Elephant\n");
    }
    else
    {
        printf("Alien\n");
    }


	return 0;
}