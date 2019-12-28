package com.company;
//Given an unsorted array return whether an increasing subsequence of length 3 exists or not in the array.
//They can be discontinuous
public class Main {
    public static boolean increasingTriplet(int[] nums) {
        int len=nums.length,index,temp1,temp2;
        for(int i=0;i<len-2;i++){
            temp1=nums[i];
            for(int j=i+1;j<len-1;j++){
                if(nums[j]>temp1){
                    temp2=nums[j];
                    for(int k=j+1;k<len;k++){
                        if(nums[k]>temp2){
                            return true;
                        }
                    }
                }
            }
        }
        return false;
    }

    public static void main(String[] args) {
	int[] nums={5,1,5,5,2,5,4};
	boolean res=increasingTriplet(nums);
	System.out.println(res);
    }
}
