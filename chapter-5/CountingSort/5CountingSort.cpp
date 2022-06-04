#include<bits/stdc++.h>

using namespace std;

void countingSort(int arr[], int n) {
    int out[10];
    int count[10];
    int max = arr[0];

    for(int i=1;i<n;i++) {
        if (arr[i]>max)
        max = arr[i];
    }
    for(int i=0;i<=max;++i) {
        count[i] = 0;
    }

    for(int i=0;i<n;i++) {
        count[arr[i]]++;
    }

    for(int i=1;i<=max;i++) {
        count[i] += count[i-1];
    }

    for(int i = n-1;i>=0;i--){
        out[count[arr[i]] - 1] = arr[i];
        count[arr[i]]--;
    }

    for(int i = 0; i < n; i++){
        arr[i] = out[i];
    }
}

void display(int arr[], int n){
    cout<<endl<<"Sorted array using Counting Sort is: ";
    for (int i = 0; i < n; i++)
        cout << arr[i] << " ";
  cout << endl;
}

int main() {
int n, i;
	cout<<"Enter the number elements in the array: ";
	cin>>n;

	int arr[n];
	for(i = 0; i < n; i++){
		cout<<"Enter element "<<i+1<<": ";
		cin>>arr[i];
	}

    countingSort(arr, n);
    display(arr, n);
}
