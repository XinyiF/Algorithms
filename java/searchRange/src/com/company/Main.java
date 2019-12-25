package com.company;
//Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.
//
//Your algorithm's runtime complexity must be in the order of O(log n).
//
//If the target is not found in the array, return [-1, -1].
//


public class Main {
    public static int[] searchRange(int[] nums, int target){
        int[] res={-1,-1};
        int mid,left=0,right=nums.length-1;
        while(left<=right){
            mid=left+(right-left)/2;
            if(nums[mid]==target){
                int low=searchlow(nums,left,mid,target);
                int high=searchhigh(nums,mid,right,target);
                res[0]=low;
                res[1]=high;
                return res;
            }
            else if(nums[mid]>target){
                right=mid-1;
            }
            else {
                left=mid+1;
            }
        }
        return res;
    }

    public static int searchlow(int[] nums,int left,int right,int key){
        while(right>=left){
            int mid=left+(right-left)/2;
            if(nums[left]==key){
                return left;
            }
            else if(nums[left]<key){
                left+=1;
            }
            else {
                right=mid-1;
            }
        }
        return -1;
    }

    public static int searchhigh(int[] nums,int left,int right,int key){
        while(right>=left){
            int mid=left+(right-left)/2;
            if(nums[right]==key){
                return right;
            }
            else if(nums[right]>key){
                right-=1;
            }
            else {
                left=mid+1;
            }
        }
        return -1;
    }

    public static void main(String[] args) {
        int [] nums={2,2};
        int target=2;
	int [] res=searchRange(nums,target);
	System.out.println(res[0]);
        System.out.println(res[1]);
	}
}
