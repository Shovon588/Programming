#include<stdio.h>
#include<string.h>
int main()
{
	#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	#endif

    int n,i;
    scanf("%d",&n);
    int a[n],count=0,tfive=0,fifty=0,hundred=0;

    for(i=0;i<n;i++)
    {
    	scanf("%d",&a[i]);
    }

    for(i=0;i<n;i++)
    {
    	if(a[i]==25)
    	{
            tfive++;
    		count++;
    	}
    	else if(a[i]==50 && tfive>=1)
    	{
    		count++;
            fifty++;
            tfive--;
    	}
    	else if(a[i]==100)
    	{
           if(fifty==0)
           {
                if(tfive>=3)
                {
                    count++;
                    hundred++;
                    tfive=tfive-3;
                }
           }
            else if(fifty>=1 && tfive>=1)
            {
                count++;
                hundred++;
                fifty--;
                tfive--;
            }
            else
            {
                break;
            }
    	}
    	else
    	{
    		break;
    	}
    }

    if(count==n)
    {
    	printf("YES\n");
    }
    else

    {
    	printf("NO\n");
    }

}