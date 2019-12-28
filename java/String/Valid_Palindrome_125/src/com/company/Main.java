package com.company;
//Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
//
//Note: For the purpose of this problem, we define empty string as valid palindrome.
//


public class Main {
    public static boolean IsNum(String n){
        for (int i = 0; i < n.length(); i++){
            if (!Character.isDigit(n.charAt(i))){
                return false;
            }
        }
        return true;
    }

    public static boolean IsLetter(String n){
        char c = n.charAt(0);
        if (((c >= 'a' && c <= 'z') || (c >= 'A' && c <= 'Z'))) {
            return true;
        } else {
            return false;
        }
    }

    public static boolean isPalindrome(String s) {
        if(s.length()==0){
            return true;
        }
        int i=0,j=s.length()-1;
        while(i<j){
            if((IsNum(String.valueOf(s.charAt(i)))||IsLetter(String.valueOf(s.charAt(i))))&&(IsNum(String.valueOf(s.charAt(j)))||IsLetter(String.valueOf(s.charAt(j))))){
                if(String.valueOf(s.charAt(i)).equalsIgnoreCase(String.valueOf(s.charAt(j)))){

                    i++;
                    j--;
                }
                else {
                    return false;
                }
            }
            else {
                if(!(IsNum(String.valueOf(s.charAt(i)))||IsLetter(String.valueOf(s.charAt(i))))){
                    i++;
                }
                else {
                    j--;
                }
            }
        }
        return true;
    }

    public static void main(String[] args) {
	String str="0P";
	boolean res= isPalindrome(str);
	System.out.println(res);
    }
}
