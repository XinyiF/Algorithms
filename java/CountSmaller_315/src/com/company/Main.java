package com.company;
//You are given an integer array nums and you have to return a new counts array.
// The counts array has the property where counts[i] is the number of smaller elements to the right of nums[i].

import java.util.Collections;
import java.util.LinkedList;
import java.util.List;

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



    public static List<Integer> countSmaller(int[] nums){
        if(nums.length==0){
            List<Integer> count = new LinkedList<>();
            return count;
        }
        List<Integer> count = new LinkedList<>(Collections.nCopies(nums.length, 0));
        int i;
        for(i=nums.length-2;i>=0;i--){
            int left=i+1,right=nums.length-1,mid;
            ShellSort(nums,i+1);
            if(nums[left]<nums[i]&&nums[right]>nums[i]){
                while(left<right){
                    mid=left+(right-left)/2;
                    if(nums[mid]<=nums[i]){
                        left=mid+1;
                    }
                    else {
                        right=mid-1;
                    }
                }

                if(i<nums.length-2){
                    left-=1;
                }

                count.set(i,left-i);
            }
            else if(nums[right]<nums[i]){
                count.set(i,right-i);
            }
            else {
                count.set(i,0);
            }
        }
        return count;
    }

    public static List<Integer> countSmaller1(int[] nums){
        if(nums.length==0){
            List<Integer> count = new LinkedList<>();
            return count;
        }
        List<Integer> count = new LinkedList<>(Collections.nCopies(nums.length, 0));
        int i,j;
        for(i=nums.length-2;i>=0;i--){
            int left=i+1,right=nums.length-1,mid;
            ShellSort(nums,i+1);
            for(j=i+1;j<nums.length;j++){
                if(nums[j]>=nums[i]){
                    break;
                }
            }
            count.set(i,j-1-i);
        }
        return count;
    }


    public static void main(String[] args) {
        int[] nums={2,3,4,2,1,7,10};
        List<Integer> count = countSmaller1(nums);
        System.out.println(count);
    }
}
