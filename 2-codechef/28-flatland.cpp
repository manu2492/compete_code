#include <iostream>
#include<bits/stdc++.h>
using namespace std;

int main() {
    int t;
    cin>>t;
    while(t--)
    {
        int n
        int count = 0;
        cin>>n;
        while(n>0)
        {
            int s = floor(sqrt(n));
            count++;
            n = n-(s*s);
        }
        cout<<count<<endl;
    }
    return 0;
}
