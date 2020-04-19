#include<bits/stdc++.h>
using namespace std;
int main()
{
	#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	#endif


    int pointA,pointB,timeA,timeB,temp1,temp2,finalA,finalB;
    scanf("%d%d%d%d",&pointA,&pointB,&timeA,&timeB);

    temp1=(3*pointA)/10;

    temp2=(pointA-(pointA/250)*timeA);

    if(temp1>=temp2)
    {
    	finalA=temp1;
    }
    else
    {
    	finalA=temp2;
    }

    temp1=(3*pointB)/10;

    temp2=(pointB-(pointB/250)*timeB);


    if(temp1>=temp2)
    {
    	finalB=temp1;
    }
    else
    {
    	finalB=temp2;
    }


    if(finalA>finalB)
    {
    	printf("Misha\n");
    }
    else if(finalA<finalB)
    {
    	printf("Vasya\n");
    }
    else
    {
    	printf("Tie\n");
    }


}