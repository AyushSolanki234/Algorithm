#include<iostream>

using namespace std;

int kadane(int array[],int length) {
   int highestMax = 0;
   int currentMax = 0;
   for(int i = 0; i < length; i++){
      currentMax =max(array[i],currentMax + array[i]) ;
      highestMax = max(highestMax,currentMax);
   }
   return highestMax;
}
int main() {
   cout << "Enter the array length: ";
   int l;
   cin >> l;
   int arr[l];
   cout << "Enter the elements of array: ";
   for (int i = 0; i < l; i++) {
      cin >> arr[i];
   }
   cout << "The Maximum Sum is: "<<kadane(arr,l) << endl;
   return 0;
}