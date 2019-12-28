package com.company;
//get the length of the last word
public class Main {
  public static int lengthOfLastWord(String s) {
    char [] array=s.toCharArray();
    int len = array.length,i,res=0;
    for (i=len-1;i>=0;i--){
        if(array[i]!=' '){
            break;
        }
    }
    for(int j=i;j>=0;j--){
        if(array[j]==' '){
            break;
        }
        res+=1;
    }
    return res;
  }

  public static void main(String[] args) {
    String s = "a   bcd  ";
    int len = lengthOfLastWord(s);
    System.out.println(len);
  }
}
