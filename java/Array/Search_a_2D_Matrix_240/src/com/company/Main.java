package com.company;

//Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:
//
//Integers in each row are sorted in ascending from left to right.
//Integers in each column are sorted in ascending from top to bottom.

import java.util.HashMap;
import java.util.Map;

public class Main {
    public static boolean searchMatrix(int[][] matrix, int target) {
        if(matrix.length==0){
            return false;
        }
        Map<Integer,Integer> count = new HashMap<>();
        int up,down,mid1,left,right,mid2,len1=matrix[0].length,len2=matrix.length;
        for(int i=0;i<len2;i++){
            for(int j=0;j<len1;j++){
                count.put(i*len1+j,matrix[i][j]);
            }
        }
        if(count.containsValue(target)){
            return true;
        }
        return false;
    }

    public static void main(String[] args) {
	int [][] max={{1,3,5,7},{2,5,6,10}};
	boolean res=searchMatrix(max,11);
	System.out.println(res);
    }
}
