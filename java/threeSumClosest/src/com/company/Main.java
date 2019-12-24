package com.company;
//Given an array nums of n integers and an integer target,
// find three integers in nums such that the sum is closest to target.
// Return the sum of the three integers.
// You may assume that each input would have exactly one solution.


import java.util.Arrays;

public class Main {
    public static int threeSumClosest(int[] nums, int target){
        Arrays.sort(nums);//-4,-1,1,2
        int new_sum=nums[0]+nums[1]+nums[nums.length-1];
        int sub1,sub2;
        for(int i=0;i<nums.length-2;i++){
            int left=i+1,right=nums.length-1;
            while(left<right){
                int old_sum=nums[i]+nums[left]+nums[right];
                sub1=Math.abs(target-old_sum);
                sub2=Math.abs(target-new_sum);
                if(old_sum==target){return old_sum;}
                else if(old_sum<target){left++;}
                else {right--;}
                if(sub1<sub2){new_sum=old_sum;}
            }
        }
        return new_sum;
        }


    public static void main(String[] args) {
	int[] nums={-1,2,1,-4};
	int target =1;
	int re=threeSumClosest(nums,target);
	System.out.println(re);
    }
}
