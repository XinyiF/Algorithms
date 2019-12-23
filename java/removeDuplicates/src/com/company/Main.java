package com.company;

public class Main {
    public static int removeDuplicates(int [] nums){
        if (nums.length == 0) return 0;
        int i = 0;
        for (int j = 1; j < nums.length; j++) {
            if (nums[j] != nums[i]) {
                i++;
                nums[i] = nums[j];
            }
        }
        return i + 1;
    }

    public static void main(String[] args) {
	int[] nums={0,0,1,1,1,2,2,3,3,4};
        int re=removeDuplicates(nums);
        System.out.println(re);
        for(int i=0;i<nums.length;i++){
            System.out.println(nums[i]);
        }
    }
}
