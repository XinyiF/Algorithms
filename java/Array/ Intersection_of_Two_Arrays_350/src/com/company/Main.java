package com.company;
//Given two arrays, write a function to compute their intersection.
import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

public class Main {
    public static int[] intersect(int[] nums1, int[] nums2) {
        Map<Integer,Integer> count=new HashMap<>();
        int len1=nums1.length,len2=nums2.length;
        if(len1>=len2){
            for(int i =0;i<len1;i++){
                if(!count.containsKey(nums1[i])){
                    count.put(nums1[i],1);
                }
                else {
                    count.put(nums1[i],count.get(nums1[i])+1);
                }
            }
            int k=0;
            for(int i=0;i<len2;i++){
                if(count.containsKey(nums2[i])&&count.get(nums2[i])>0){
                    nums1[k]=nums2[i];
                    count.put(nums2[i],count.get(nums2[i])-1);
                    k++;
                }
            }
            return Arrays.copyOfRange(nums1,0,k);
        }
        else {
            for(int i =0;i<len2;i++){
                if(!count.containsKey(nums2[i])){
                    count.put(nums2[i],1);
                }
                else {
                    count.put(nums2[i],count.get(nums2[i])+1);
                }
            }
            int p=0;
            for(int i=0;i<len1;i++){
                if(count.containsKey(nums1[i])&&count.get(nums1[i])>0){
                    nums2[p]=nums1[i];
                    count.put(nums1[i],count.get(nums1[i])-1);
                    p++;
                }
            }
            return Arrays.copyOfRange(nums2,0,p);
        }

    }

    public static void main(String[] args) {
	int []num1={1,2,3,4,3,4},num2={2,3,4};
	int [] res=intersect(num1,num2);
	for(int i=0;i<res.length;i++){
	    System.out.println(res[i]);
    }
    }
}
