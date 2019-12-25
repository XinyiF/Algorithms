package com.company;

public class Main {
    public static void ShellSort(int[] nums){
        int len=nums.length;
        int step=len/2;
        while(step>0){
            for(int i=0;i<step;i++){
                for(int j=i+step;j<len;j+=step){
                    int temp;
                    for(int k=j-step;k>=0;k-=step){
                        if(nums[k]>nums[j]){
                            temp=nums[k];
                            nums[k]=nums[j];
                            nums[j]=temp;
                        }
                    }
                }
            }
            step/=2;
        }
    }

    public static void main(String[] args) {
        int [] nums={2,4,5,3,32,33,12,32,0,1,2,3};
        ShellSort(nums);
        for(int i=0;i<nums.length;i++){
            System.out.println(nums[i]);
        }
    }
}
