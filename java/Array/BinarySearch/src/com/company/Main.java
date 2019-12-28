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
    public static int[] sortValues(int[] a){
        for(int j=a.length-1;j>=0;j--){
            for(int i=0;i<j;i++){
                if(a[i]>a[i+1]){
                    int low=a[i+1];
                    a[i+1]=a[i];
                    a[i]=low;
                }
            }
        }

        return a;
    }

    public static void main(String[] args) {
        int[] a={6,5,7,55,32,34,19};
        int key=5;
        sortValues(a); /*rearrange it from low to high*/
        int r=rank(key,a);
        System.out.println(r);
    }
}

