package com.company;
//Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.
//
//You may assume that the array is non-empty and the majority element always exist in the array.

import java.util.HashMap;
import java.util.Map;

public class Main {
    private static Map<Integer,Integer> count(int[] nums){
        Map<Integer, Integer> counts = new HashMap<Integer, Integer>();
        for(int i=0;i<nums.length;i++){
            if(!counts.containsKey(nums[i])){
                counts.put(nums[i],1);
            }
            else{
                counts.put(nums[i],counts.get(nums[i])+1);
            }
        }
        return counts;
    }

    public static int majorityElement(int[] nums){
        Map<Integer,Integer> res=count(nums);

        for(int i=0;i<nums.length;i++){
            if(res.get(nums[i])>nums.length/2){
                return nums[i];
            }
        }
        return -1;
    }

    public static void main(String[] args) {
        int [] nums={2,2,3,4,5,2,2,2,2};
        int res=majorityElement(nums);
        System.out.println(res);


    }
}
