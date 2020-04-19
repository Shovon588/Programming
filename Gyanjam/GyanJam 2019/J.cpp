#include <bits/stdc++.h>

using namespace std;

typedef long long int ll;

map <ll,ll> mm;
map <ll,ll>::iterator mt;

ll prime[1000000];

void sieve(){

    memset(prime,true,sizeof prime);
    for (ll i=2; i*i<1000000;i++){
        if (prime[i]){
            for (ll j=i*i; j<1000000; j+=i)
                prime[j] = false;
        }
    }

}

int main(){

    sieve();

    ll a, b;

    scanf("%lld %lld,", &a, &b);

    for (ll i=1; i<=sqrt(a); i++){
        if (a%i==0){
            mm[i]++;
            mm[a/i]++;
        }
        else if (a/i==i) mm[i]++;
    }

    for (ll i=1; i<=sqrt(b); i++){
        if (b%i==0){
            mm[i]++;
            mm[b/i]++;
        }
        else if (b/i==i) mm[i]++;
    }

    ll sum = 0;

    for (mt=mm.begin(); mt!=mm.end(); mt++){
        //cout << mt->first << " " << mt->second << endl;
        if (mt->second>1)
            sum+=mt->first;
    }

    printf("%lld\n", sum);

   // printf("%lld\n", prime[5]);

    return 0;

}
