// o(n log n)
#include <bits/stdc++.h>
using namespace std;

int main()
{
    int t;
    cin >> t;

    while (t--)
    {
        int n;
        cin >> n;
        int arr[n];

        for (int i = 0; i < n; i++)
        {
            cin >> arr[i];
        }
        sort(arr, arr+n);
        int sum=arr[0]+arr[1];
        
        cout<<sum<<endl;
    }
    return 0;
}


