package com.company;
//Given a string, find the first non-repeating character in it and return it's index.
// If it doesn't exist, return -1.

import java.util.HashMap;
import java.util.Map;

public class Main {
    public static int firstUniqChar(String s) {
        Map<Character,Integer> count=new HashMap<>();
        for(int i=0;i<s.length();i++){
            if(!count.containsKey(s.charAt(i))){
                count.put(s.charAt(i),1);
            }
            else {
                count.put(s.charAt(i),count.get(s.charAt(i))+1);
            }
        }
        for(int i=0;i<s.length();i++){
            if(count.get(s.charAt(i))==1){
                return i;
            }
        }
        return -1;
    }

    public static void main(String[] args) {
	String s="loveleetcode";
	int res=firstUniqChar(s);
	System.out.println(res);
    }
}
