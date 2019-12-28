package com.company;
//Given an array nums of n integers where n > 1,
//  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].


public class Main {
    public static int[] productExceptSelf(int[] nums) {
        int p=0,product;
        int [] res=new int[nums.length];
        for(int i=0;i<nums.length;i++){
            product=1;
            for(int j=0;j<nums.length;j++){
                if(j!=i){
                    product*=nums[j];
                }
            }
            res[p]=product;
            p++;
        }
        return res;
    }

    public static void main(String[] args) {
	// write your code here
    }
}
