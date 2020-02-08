#include <iostream>
#include <cstdlib>

template <typename genericType> void swap(genericType *element1, genericType *element2){
    typename swapValue = *element1;
    *element1 = *element2;
    *element2 = swapValue;
} 
template <typename genericType> void medianOfThree(genericType *arrLow, genericType *arrMid, genericType *arrHigh){
    //find the median of the three values and move it to the end

    //choose one possible case for the lowest index being the minimum
    if (*arrLow >= *arrMid && *arrLow <= *arrHigh){
        swap(arrLow, arrHigh);
    }
    //either arrLow is less than arrMid or greater than arrHigh
    else if (*arrMid <= *arrHigh && *arrMid > *arrLow){
        swap(arrMid, arrHigh);
    }
    //if the middle element is the median, swap with the high element

    //otherwise, keep everything the same, as the median value should be at the end of the array
}