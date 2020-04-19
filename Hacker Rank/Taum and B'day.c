#include<stdio.h>
#include<math.h>
int main()
{
	#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	#endif

    long long int b,w,x,y,z,total,t,i;
    scanf("%lld",&t);

    for(i=0;i<t;i++)
    {
        total=0;

        scanf("%lld%lld%lld%lld%lld",&b,&w,&x,&y,&z);

        if(x==y)
        {
            total=(b+w)*x;
        }
        else if(x>y)
        {
            if(((b+w)*y)+(b*z)<(b*x)+(w*y))
            {
                total=((b+w)*y)+(b*z);
            }
            else
            {
                total=(x*b)+(y*w);
            }
            
        }
        else if(y>x)
        {
            if(((b+w)*x)+(w*z)<(b*x)+(w*y))
            {
                total=((b+w)*x)+(w*z);
            }
            else
            {
                total=(x*b)+(y*w);
            }
            
        }

        printf("%lld\n",total );

    }



}