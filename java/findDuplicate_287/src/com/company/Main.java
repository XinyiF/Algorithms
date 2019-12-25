package com.company;
//Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive),
// prove that at least one duplicate number must exist.
// Assume that there is only one duplicate number, find the duplicate one.
//You must not modify the array (assume the array is read only).

import java.util.Arrays;

public class Main {
    public static int findDuplicate(int[] nums){
        Arrays.sort(nums);
        int i;
        for(i=0;i<nums.length-2;i++){
            if(nums[i]==nums[i+1]){
                break;
            }
        }
        return nums[i];
    }



    public static void main(String[] args) {
	int []nums={1,3,4,2,2};
	int res=findDuplicate(nums);
	System.out.println(res);
    }
}
