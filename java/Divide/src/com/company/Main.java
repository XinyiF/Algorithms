package com.company;

public class Main {
    public static int divide(int dividend, int divisor){
        int flag1=0;
        int flag2=0;
        if(divisor>0){
            divisor=-divisor;
            flag1=1;
        }
        if(dividend>0){
            dividend=-dividend;
            flag2=1;
        }
        if(divisor<dividend) {
            return 0;
        }
        if(divisor==dividend) {
            if(flag1!=flag2){
                return -1;
            }
            else{
                return 1;
            }
        }

        int low=dividend;
        int high=0;
        int mid=0;
        while(low<high){
            mid=-(high-(high-low)/2);
            if(mid*divisor==dividend){
                if(flag1!=flag2){
                    mid=-mid;
                }
                return mid;
            }
            else if(mid*divisor<dividend){
                low=-mid;
            }
            else{
                high=high-1;
            }
        }
        if(dividend==-2147483647||dividend==-2147483648){
            mid+=1;
        }


        if(flag1!=flag2){
            mid=-mid;
        }
        return mid;
    }


    public static void main(String[] args) {
        int re=divide(-2147483648,-1);
        int minn=Math.m[]
        System.out.println(re);
        System.out.println(2147483647+1);
    }
}
