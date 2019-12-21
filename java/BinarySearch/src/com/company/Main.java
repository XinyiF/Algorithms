package com.company;


public class Main {
    public static int rank(int key ,int[] a){
        int low=0;
        int high=a.length;/*the number of values in the array = 7*/
        int mid= low + (high - low) / 2; /*0+3*/
        while(low<high) {
            if (a[mid] < key) {
                low = low + 1;
            } else if (a[mid] > key) {
                high = high - 1;
            } else {
                break;
            }
            mid = low + (high - low) / 2;
        }
        return mid;
    }

    public static void main(String[] args) {
        int[] a={3,5,7,8,10,14,19};
        int key=5;
        int r=rank(key,a);
        System.out.println(r);
    }
}
