#include <stdio.h>
#define ARRSIZE 10
int binarySearch(int arr[], int arrLen, int target);

int main(){
    int arr[ARRSIZE] = {1, 4, 6, 7, 9, 15, 21, 98, 101, 102};
    int target = 15;
    int result = binarySearch(arr, ARRSIZE, target);
    printf("The index of the found value is %d \n", result);
}

int binarySearch(int arr[], int arrLen, int target){
    int right = arrLen - 1;
    int left = 0;

    while (left <= right){
        int mid = left + (right - left)/2;
        if (arr[mid] == target) return mid;
        else if (target > arr[mid]){
            left = mid + 1;
        }else if (target < arr[mid]){
            right = mid - 1;
        }
    }
    return -1;
}
