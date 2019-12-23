package com.company;

public class Main {
    public static int maxArea(int[] height){
        int old_v=0;
        int Min=0;
        for(int j=0;j<height.length-1;j++){
            int new_v=0;
            int count=1;
            for(int k=j+1;k<height.length;k++){
                Min=Math.min(height[j],height[k]);
                new_v=Min*count;
                old_v=Math.max(new_v,old_v);
                count+=1;
            }

        }
        return old_v;
    }

    public static void main(String[] args) {
        int [] a={2,3,4,5,18,17,6};
	int re=maxArea(a);
	System.out.println(re);
    }
}
