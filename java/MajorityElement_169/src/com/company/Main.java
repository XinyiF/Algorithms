package com.company;
//Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.
//
//You may assume that the array is non-empty and the majority element always exist in the array.
//

public class Main {
  public static int Boyer_Moore(int[] nums) {
    int i, j, count = 0;
    for (i = 0; i < nums.length; i++) {
      for (j = 0; j < nums.length; j++) {
        if (nums[j] == nums[i]) {
          count += 1;
        } else {
          count -= 1;
        }
      }
      if (count > 0) {
        break;
      } else {
        count = 0;
      }
    }
    return nums[i];
  }

  public static void main(String[] args) {
    int[] nums = {-1, 100, 2, 100, 100, 4, 100};
    int res = Boyer_Moore(nums);
    System.out.println(res);
  }
}
