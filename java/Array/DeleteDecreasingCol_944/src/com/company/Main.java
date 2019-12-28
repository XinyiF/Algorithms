package com.company;

import javax.xml.stream.XMLInputFactory;

//count how many cols are decreasing
public class Main {
    public static int minDeletionSize(String[] A) {
        int rows=A.length,cols=A[0].length(),count=0;
        for(int i=0;i<cols;i++){
            for(int j=0;j<rows-1;j++){
                if(A[j].charAt(i)>A[j+1].charAt(i)){
                    count+=1;
                    break;
                }
            }
        }
        return count;
    }

    public static void main(String[] args) {
        String[] A={"abc","dfg","ase"};
        int res= minDeletionSize(A);
        System.out.println(res);
    }
}
