package com.company;
//Given a sorted array and a target value, return the index if the target is found.
// If not, return the index where it would be if it were inserted in order.
//
//You may assume no duplicates in the array.
//


public class Main {
    public static int searchInsert(int[] nums, int target){
        int left=0,right=nums.length-1,mid=left+(right-left)/2,flag=0;
        int find=search(nums,left,right,target,flag);
        return find;
    }

    public static int search(int[] nums,int left,int right,int key,int flag){
        int mid=0;
        while(right>=left){
            mid=left+(right-left)/2;
            if(nums[mid]==key){
                flag=1;
                return mid;
            }
            else if(nums[mid]<key){
                left=mid+1;
            }
            else {
                right=mid-1;
            }
        }
        return left;
    }

    public static void main(String[] args) {
	int [] nums={1,3,4,7,9,13,15};
	int target=19;
	int res=searchInsert(nums,target);
	System.out.println(res);
    }
}
