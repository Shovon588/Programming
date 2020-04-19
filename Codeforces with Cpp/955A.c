#include<bits/stdc++.h>
using namespace std;
int main()
{
	#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	#endif

    
    float hour,minute,hunger,hun_increase,cost,hun_decrease,time;

    float temp1,temp2;

    scanf("%f%f",&hour,&minute);
    scanf("%f%f%f%f",&hunger,&hun_increase,&cost,&hun_decrease);

    temp1=(hunger/hun_decrease);
    temp1=ceil(temp1);
    temp1=(temp1*cost);


    if(hour<20 && minute==0)
    {
    	time=(20-hour)*60;
    }
    else if(hour<20)
    {
    	time=((19-hour)*60)+(60-minute);
    }
    else if(hour>=20)
    {
    	temp1=temp1-(temp1*.2);
    }


    temp2=time*hun_increase;
    temp2=temp2+hunger;
    temp2=temp2/hun_decrease;

    temp2=ceil(temp2);
    cost=cost-(cost*0.2);

    temp2=temp2*cost;

 	if(temp1<=temp2)
 	{
 		printf("%f\n",temp1);
 	}
 	else 
 	{
 		printf("%f\n",temp2 );
 	}


}