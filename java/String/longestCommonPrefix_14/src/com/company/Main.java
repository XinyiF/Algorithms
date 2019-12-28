package com.company;

public class Main {

    public static String longestCommonPrefix(String[] strs) {
        if(strs.length==0){
            return "";
        }
        String perfix=strs[0];
        int len;
        for(int i=1;i<strs.length;i++){
            while(strs[i].indexOf(perfix)!=0){
                perfix=perfix.substring(0,perfix.length()-1);
            }
        }
        return perfix;
    }

    public static void main(String[] args) {
	String[] strs={};
	System.out.print(longestCommonPrefix(strs));
    }
}
