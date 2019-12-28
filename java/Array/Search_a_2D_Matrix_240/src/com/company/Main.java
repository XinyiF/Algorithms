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
        int i=matrix.length-1,j=0;
        while(i>=0&&j<=matrix[0].length-1){
            if(matrix[i][j]>target){
                i--;
            }
            else if(matrix[i][j]<target){
                j++;
            }
            else {
                return true;
            }
        }
        return false;
    }

    public static void main(String[] args) {
	int [][] max={{1,3,5,7},{2,5,6,10}};
	boolean res=searchMatrix(max,10);
	System.out.println(res);
    }
}
