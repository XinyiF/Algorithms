package com.company;

import java.text.DecimalFormat;

public class Main {
    public static double dice(int sum){
        int[] a={1,2,3,4,5,6};
        int[] b={1,2,3,4,5,6};
        int count=0;
        double dic=0.0;
        for(int i=0;i<a.length;i++){
            for(int j=0;j<b.length;j++){
                if(a[i]+b[j]==sum){
                    count+=1;
                }
            }
        }
        dic=(double)count/36.0;
        return dic;
    }

    public static void main(String[] args) {
        double dic=dice(5);
        System.out.println(dic);


    }
}
