package com.company;
//Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
//You are given a target value to search. If found in the array return its index, otherwise return -1.
//You may assume no duplicate exists in the array.
//Your algorithm's runtime complexity must be in the order of O(log n).


public class Main {
    public static int search(int[] nums, int target) {
        int left = 0;
        int right = nums.length - 1;
        while(left<=right){
            int mid = (right + left) / 2;
            if(nums[mid]==target){return mid;}
            else if(nums[mid]<nums[right]){
                if(nums[mid]<target&&nums[right]>=target){
                    left=mid;
                }
                else{
                    right=mid;
                }
            }
            else{
                if (nums[mid]>target&&nums[left]<=target){
                    right=mid;
                }
                else {left=mid;}
            }
        }
        return -1;
    }


    public static void main(String[] args) {
	int [] nums={};
	int target=0;
	int re=search(nums,target);
	System.out.println(re);
    }
}
