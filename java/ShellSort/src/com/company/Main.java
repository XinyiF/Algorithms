package com.company;

public class Main {
    public static void ShellSort(int[] nums,int star){
        int len=nums.length-star;
        int step=len/2;
        while(step>0){
            for(int i=star;i<star+step;i++){
                for(int j=nums.length-1;j>star;j-=step){
                    int temp;
                    for(int k=j-step;k>=star;k-=step){
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
        int [] nums={5,2,6,1,3,9,8,10,12,54,13,11};//5131269 5121369 5112369
        ShellSort(nums,2);
        for(int i=0;i<nums.length;i++){
            System.out.println(nums[i]);
        }
    }
}
