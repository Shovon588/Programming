/* HDU3140 Money Matters */

#include <bits/stdc++.h>

using namespace std;

const int N = 10000;
int f[N], w[N];

void UFInit(int n)
{
    for(int i = 0; i < n; i++)
        f[i] = i;
}

int Find(int a) {
    return a == f[a] ? a : f[a] = Find(f[a]);
}

void Union(int a, int b)
{
    a = Find(a);
    b = Find(b);
    if (a != b) {
        f[a] = b;
        w[b] += w[a];
    }
}

int main()
{
    int n, m;
    while(~scanf("%d%d", &n, &m)) {
        UFInit(n);

        for(int i = 0; i < n; i++)
            scanf("%d", &w[i]);

        for(int i = 0; i < m; i++) {
            int u, v;
            scanf("%d%d", &u, &v);
            Union(u, v);
        }

        int i;
        for(i = 0; i < n; i++)
            if(w[Find(i)] != 0)
                break;

        puts(i == n ? "POSSIBLE" : "IMPOSSIBLE");
    }

    return 0;
}
 ———————————————— 
版权声明：本文为CSDN博主「海岛Blog」的原创文章，遵循CC 4.0 by-sa版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/tigerisland45/article/details/89838378
