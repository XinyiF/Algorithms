package com.company;

public class Main {
    public static void InsertSort(int [] nums){
        for(int i=1;i<nums.length;i++){
            int j;
            int temp=nums[i];
            for(j=i-1;j>=0;j--){
                if(temp>=nums[j]){
                    break;
                }
                else{
                    nums[j+1]=nums[j];
                }
            }
            nums[j+1]=temp;
        }
    }

    public static void BinaryInsertSort(int [] nums){
        for(int a=1;a<nums.length;a++){
            int tep=nums[a];
           int low=0;
           int high=a;
           int mid=low+(high-low)/2;
           if(nums[mid]<tep){
               low=mid;
           }
           else if(nums[mid]>tep){
               high-=1;
           }
           else {
               for(int k=a-1;k>mid;k--){
                   nums[k+1]=nums[k];
               }
               nums[mid+1]=tep;
           }
        }
        }


    public static void main(String[] args) {
	int [] nums={1,2,4,5,2,2,5,6,9,7,7};
	InsertSort(nums);

	for(int k=0;k<nums.length;k++){
	    System.out.println(nums[k]);
    }
    }
}
