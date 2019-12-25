package com.company;
//A peak element is an element that is greater than its neighbors.
//
//Given an input array nums, where nums[i] ≠ nums[i+1], find a peak element and return its index.
//
//The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.
//
//You may imagine that nums[-1] = nums[n] = -∞.
//

public class Main {
    public static int findPeakElement(int[] nums){
        int len=nums.length,left=0,right=len-1,mid;
        while (left<right-1){
            mid=left+(right-left)/2;
            if(nums[mid+1]>nums[mid]){
                left=mid;
            }
            else {
                right=mid;
            }
        }
        if(nums[left]>nums[right]){
            return left;
        }
        else {
            return right;
        }
        }

    public static void main(String[] args) {
        int []nums={2,1};
        int res=findPeakElement(nums);
        System.out.println(res);

    }
}
