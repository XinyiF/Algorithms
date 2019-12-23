package com.company;

public class Main {
    public static void nextPermutation(int[] nums){
        int i;
        for(i=nums.length-1;i>0;i--){
            if(nums[i-1]<nums[i]){
                i=i-1;
                int j;
                for(j=i;j<nums.length;j++){
                    if(nums[j]<nums[i]){
                        break;
                    }
                }
                j=j-1;
                swap(nums,i,j);
                break;
            }
        }
        for(int k=nums.length-1;k<i;k--){
            if(nums[k-1]>nums[k]){
                swap(nums,k,k-1);
                System.out.println("HI");
                break;
            }
        }

    }






    private static void swap(int[] nums, int i, int j) {
        int temp = nums[i];
        nums[i] = nums[j];
        nums[j] = temp;
    }


    public static void main(String[] args) {
        int[] nums={1,3,2};
        nextPermutation(nums);
        for(int i=0;i<nums.length;i++){
            System.out.println(nums[i]);
        }

    }
}
