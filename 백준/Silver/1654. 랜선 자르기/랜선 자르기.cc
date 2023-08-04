#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int n, k;
long long ans;
vector <int> v;

void make_lan(long long left, long long right) {
	while (left <= right) {
		long long mid = (left + right) / 2;
		int cnt = 0;
		for (int i = 0; i < k; i++) {
			cnt += v[i] / mid;
		}
		if (cnt < n) right = mid - 1;
		else {
			ans = max(mid,ans);
			left = mid + 1;
		}
	}
	cout << ans;
	return;
}

int main()
{
	cin >> k >> n;
	for (int i = 0; i < k; i++) {
		long long a;
		cin >> a;
		v.push_back(a);
	}
	sort(v.begin(), v.end());
	make_lan(1, v[k-1]);
}