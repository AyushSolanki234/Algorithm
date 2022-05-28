#include<iostream>

 using namespace std;

 int main(){
     int n;
    cout<<"Enter the number of array: ";
    cin>>n;
    int arr[n];
    for(int i=0;i<n;i++){
        cin>>arr[i];
    }

    for(int i=0;i<n-1;i++){
        int min1 = i;
        for(int j=i+1;j<n;j++){
            if(arr[min1]>arr[j]){
                min1 = j;
            }
        }
        int temp = arr[min1];
        arr[min1] = arr[i];
        arr[i] = temp;
    }

     cout<<"The Selection sort is: "<<" ";
    for(int i=0;i<n;i++){
        cout<<arr[i]<<" ";
    }
 }
