#include<bits/stdc++.h>

#define ll long long 
using namespace std;
int main()
{
	ll p1, p2, p3, w;

  cin >> p1 >> p2 >> p3 >> w;


  vector < ll > arr;

  arr.clear();

  arr.push_back(p1);
  arr.push_back(p2);
  arr.push_back(p2);

  sort(arr.begin(), arr.end());

  if(arr[2]+arr[1] >= w)
  {cout << "YES" << endl;}
else
{
  cout << "NO" << endl;
}

return 0;
}