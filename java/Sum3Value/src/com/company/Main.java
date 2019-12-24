package com.company;

import java.lang.reflect.Array;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Main {
    public static List<List<Integer>> threeSum(int[] nums){
        List<List<Integer>> ans = new ArrayList();
        if(nums.length<3){
            return ans;
        }
        Arrays.sort(nums);//-4,-1,-1,0,1,2
        int i=0;
        int left=1,right=nums.length-1,sum=0;
        for(i=0;i<nums.length-3;i++){
            while(left<right){
                sum=nums[i]+nums[left]+nums[right];
                if(sum==0){
                    ans.add(Arrays.asList(nums[i],nums[left],nums[right]));
                    right-=1;left+=1;
                }
                else if(sum>0){right-=1;}
                else{left+=1;}
                while(left<right&&nums[left]==nums[left+1]){left+=1;}
                while(left<right&&nums[right]==nums[right-1]){right-=1;}
            }
        }

        return ans;
    }

    public static void main(String[] args) {
	int [] nums={-1, 0, 1, 2, -1, -4};
        List<List<Integer>> ans=threeSum(nums);
        /*
        for (int i = 0; i < ans.size(); i++) {
            System.out.println(ans.get(i));
        }
        */
        System.out.println(ans[0][0]);


    }
}
