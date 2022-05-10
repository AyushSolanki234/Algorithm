#include<iostream>

using namespace std;

 //for sorting
void sorting(int arr[],int n){
    for(int i=0;i<n;i++){
        int temp=0;
        for(int j=0;j<n-1-i;j++){
            if(arr[j]>arr[j+1]){
                temp = arr[j];
                arr[j] = arr[j+1];
                arr[j+1] = temp;
            }
        }
    }
}

void display(int arr[],int n){
    for(int i=0;i<n;i++){
        cout<<arr[i]<<" ";
    }
    cout<<endl;
}

int binary(int arr[],int n,int key){
    int start=0;
    int end1 = n-1;
    while(end1>=start){
        int mid = (start+end1)/2;
        if(arr[mid]==key){
            return mid;
//           cout<<"element found in "<<mid<<" location";
//           break;
        }
        else if(arr[mid]<key){
            start = mid +1;
        }
        else if(arr[mid]>key){
            end1 = mid-1;
        }
    }
    return -1;
}

int main(){
    int n,key;
    cout<<"Enter the size of array = ";
    cin>>n;

    int arr[n];
    cout<<"Enter the "<<n<< " element in array = ";
    for(int i=0;i<n;i++){
        cin>>arr[i];
    }
    cout<<"Enter the number for searching = ";
    cin>>key;

   sorting(arr,n);
   cout<<"sorting array is : ";
   display(arr,n);

    if(binary(arr,n,key)!=-1){
        cout<<"Element Found!. IN "<<binary(arr,n,key)<<" Index";
    }
    else{
        cout<<"Element Not Found!";
    }
    return 0;
}
