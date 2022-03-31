#include <iostream>
using namespace std;

int main() {
	int t;
	cin>>t;
	while(t--)
	{
	    int n;
	    int b;
	    cin>>n>>b;
	    long w,h,p;
	    int max = 0;
	    for(int i=1;i<=n;i++)
	    {
	        cin>>w>>h>>p;
	        int area=w*h;
	        if(p<=b)
	        {
	            if(area>max)
	            max=area;
	        }
	    }
	    if(max == 0)
	    {
	        cout<<"no tablet"<<endl;
	    }
	    else
	    {
	        cout<<max<<endl;
	    }
	    cout<<endl;
	}
	return 0;
}
