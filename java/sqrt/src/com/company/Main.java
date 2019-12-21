package com.company;

import static java.lang.StrictMath.random;

public class Main {
    public static double fuc(double a,double b){  /*a is the unknown*/
        double fx;
        fx=a*a-b;
        return fx;
    }
    public static double dot(double a,double b){
        double fx;
        fx=2*a;
        return fx;
    }
    public static double sqrt(double value){
        double a=value+1;
        double flag;
        while(fuc(a,value)>=1e-15){
            double dot=dot(a,value);
            a=((-fuc(a,value))/dot)+a;
        }
        return a;
    }

    public static void main(String[] args) {
        double value=5;
        double root=sqrt(value);
        System.out.println(random());
        System.out.println(root);
    }
}
