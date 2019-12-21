package Array;

public class CopyArray {
    public static void main(String[] args){
        int[] copyFrom={1,2,3,4};
        int[] copyTo=new int[2];
        /*first number means get value from copyFrom[1],0 means put value into copyTo, begin from copyTo[0], fill 2 values*/
        System.arraycopy(copyFrom,1,copyTo,0,2);
        System.out.println(copyTo[1]);
    }
}
