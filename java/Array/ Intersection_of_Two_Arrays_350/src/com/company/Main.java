package com.company;
//Given two arrays, write a function to compute their intersection.
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;

public class Main {
    public static int[] intersect(int[] nums1, int[] nums2) {
        Map<Integer,Integer> count1=new HashMap<>();
        Map<Integer,Integer> count2=new HashMap<>();
        ArrayList<Integer> array=new ArrayList<>();
        int len1=nums1.length,len2=nums2.length,index=0;
        for(int i=0;i<len1;i++){
            count1.put(i,nums1[i]);
        }
        for(int i=0;i<len2;i++){
            count2.put(i,nums2[i]);
        }
        for(int i=0;i<len1;i++){
            for (int j=0;j<len2;j++){
                if(count1.get(i).equals(count2.get(j))){
                    index++;
                    array.add(count2.get(j));
                    count2.put(j,null);
                    break;
                }
            }
        }
        int [] res=new int[index];
        for(int i=0;i<index;i++){
            res[i]=array.get(i);
        }
        return res;
    }

    public static void main(String[] args) {
	int []num1={1,2,3,4,3,4},num2={2,3,4};
	int [] res=intersect(num1,num2);
	for(int i=0;i<res.length;i++){
	    System.out.println(res[i]);
    }
    }
}
