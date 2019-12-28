package com.company;
//Given an array nums, write a function to move all 0's to the end of it
// while maintaining the relative order of the non-zero elements.

public class Main {
    public static void moveZeroes(int[] nums) {
        int len=nums.length,temp,j=len-1;
        for(int i=len-1;i>=0;i--){
            if(nums[i]==0){
                int k=i;
                while(k+1<=j){
                    nums[k]=nums[k+1];
                    k++;
                }
                nums[j]=0;
                j--;
            }
        }
    }

    public static void main(String[] args) {
	int [] nums={1,0,2,0,4,5,6};
	moveZeroes(nums);
	for(int i=0;i<nums.length;i++){
	    System.out.println(nums[i]);
    }
    }
}
