package com.company;
//Write an algorithm to determine if a number is "happy".
//A happy number is a number defined by the following process:
// Starting with any positive integer, replace the number by the sum of the squares of its digits,
// and repeat the process until the number equals 1 (where it will stay),
// or it loops endlessly in a cycle which does not include 1.
// Those numbers for which this process ends in 1 are happy numbers.

import java.util.HashMap;
import java.util.Map;

public class Main {

    public static int count(int num){
            int val=0;
                while(num!=0){
                    val+=(Math.pow(num%10,2));
                    num=num/10;
                }
            return val;
    }

    public static boolean isHappy(int n){
        Map<Integer,Integer> sum=new HashMap<Integer, Integer>();
        int res,step=1;
        while(true){
            System.out.println(n);
            res=count(n);
            if(res==1){
                return true;
            }
            else if(sum.containsValue(res)){
                return false;
            }
            sum.put(step,res);
            step+=1;
            n=res;
        }
    }

    public static void main(String[] args) {
	int n=19;
	boolean res=isHappy(n);
	System.out.println(res);
    }
}
