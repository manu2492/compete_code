#include <bits/stdc++.h>
using namespace std;

int main() {
    int t;
    cin>>t;

    while(t--)
    {
	int n;
        cin>>n;
	int arr[n];
	set<int>ans;

	for(int i=0;i<n;i++)
	{
            cin>>arr[i];
            ans.insert(arr[i]);
        }
	   
        cout<<ans.size()<<endl;
    }
    return 0;
}


