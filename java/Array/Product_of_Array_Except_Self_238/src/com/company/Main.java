package com.company;
//Given an array nums of n integers where n > 1,
//  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].


public class Main {
    public static int[] productExceptSelf(int[] nums) {
        int[] left=new int[nums.length],right=new int[nums.length],res=new int[nums.length];
        int suml=1,sumr=1;
        left[0]=1;
        right[nums.length-1]=1;
        for(int i=1;i<nums.length;i++){
            suml*=nums[i-1];
            left[i]=suml;
        }
        for(int i=nums.length-2;i>=0;i--){
            sumr*=nums[i+1];
            right[i]=sumr;
        }
        for(int i=0;i<nums.length;i++){
            res[i]=left[i]*right[i];
        }
        return res;
    }

    public static void main(String[] args) {
	int []nums={1,2,3,4};
	int []res=productExceptSelf(nums);
        for(int i=0;i<nums.length;i++){
            System.out.println(res[i]);
        }
    }
}
