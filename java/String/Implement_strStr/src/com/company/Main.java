package com.company;
//Implement strStr().
//
//Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
//

public class Main {
    public static int strStr(String haystack, String needle) {
        int strlen=haystack.length(),subLen=needle.length(),flag=0;
        if(strlen==0){return 0;}
        if(subLen==0){return -1;}
        for(int i=0;i<strlen-subLen+1;i++){
            System.out.println("i="+i);
            if(haystack.charAt(i)==needle.charAt(0)){
                for(int j=1;j<subLen;j++){
                    System.out.println("j="+j);
                    if(haystack.charAt(i+j)==needle.charAt(j)){
                        flag+=1;
                    }
                    else {
                        flag=0;
                        break;
                    }
                }
                if(flag==subLen-1){
                    return i;
                }
            }
        }
        return -1;
    }

    public static void main(String[] args) {
	String haystack = "mississippi", needle = "issip";
	int res=strStr(haystack,needle);
	System.out.println(res);
    }
}
