package com.company;
// Given a board with m by n cells, each cell has an initial state live (1) or
// dead (0).
// Each cell interacts with its eight neighbors (horizontal, vertical, diagonal)
// using the following four rules (taken from the above Wikipedia article):

// Any live cell with fewer than two live neighbors dies, as if caused by
// under-population. Any live cell with two or three live neighbors lives on to
// the next generation. Any live cell with more than three live neighbors dies,
// as if by over-population.. Any dead cell with exactly three live neighbors
// becomes a live cell, as if by reproduction.

// Write a function to compute the next state (after one update) of the board
// given its current state. 
// The next state is created by applying the above rules simultaneously to every
// cell in the current state, where births and deaths occur simultaneously.

import java.util.HashMap;
import java.util.Map;

public class Main {
  public static int count(int[][] board, int r, int c) {
    int row = board.length, col = board[0].length, sum = 0;
    if (row >= 3 && col >= 3) {
      if (0 < r && r < (row - 1) && 0 < c && c < (col - 1)) {
        sum += board[r][c - 1] + board[r - 1][c - 1] + board[r - 1][c] +
               board[r + 1][c + 1] + board[r][c + 1] + board[r - 1][c + 1] +
               board[r + 1][c] + board[r + 1][c - 1];
      } else if (c == 0 && r == 0) {
        sum += board[r][c + 1] + board[r + 1][c + 1] + board[r + 1][c];
      } else if (c == col - 1 && r == 0) {
        sum += board[r][c - 1] + board[r + 1][c - 1] + board[r + 1][c];
      } else if (c == 0 && r == row - 1) {
        sum += board[r - 1][c] + board[r - 1][c + 1] + board[r][c + 1];
      } else if (c == col - 1 && r == row - 1) {
        sum += board[r][c - 1] + board[r - 1][c - 1] + board[r - 1][c];
      } else if (c == 0 && r > 0 && r < row - 1) {
        sum += board[r - 1][c] + board[r - 1][c + 1] + board[r][c + 1] +
               board[r + 1][c + 1] + board[r + 1][c];
      } else if (c == col - 1 && r > 0 && r < row - 1) {
        sum += board[r - 1][c] + board[r - 1][c - 1] + board[r][c - 1] +
               board[r + 1][c - 1] + board[r + 1][c];
      } else if (r == 0 && c > 0 && c < col - 1) {
        sum += board[r][c - 1] + board[r + 1][c - 1] + board[r + 1][c] +
               board[r + 1][c + 1] + board[r][c + 1];
      } else if (r == row - 1 && c > 0 && c < col - 1) {
        sum += board[r][c - 1] + board[r - 1][c - 1] + board[r - 1][c] +
               board[r - 1][c + 1] + board[r][c + 1];
      }
    }
    return sum;
  }

  public static Map<Integer, Integer> store(int[][] board) {
    Map<Integer, Integer> map = new HashMap<Integer, Integer>();
    for (int i = 0; i < board.length + 2; i++) {
      for (int j = 0; j < board[0].length + 2; j++) {
        map.put((i) * (board[0].length + 2) + (j), 0);
      }
    }
    for (int i = 1; i < board.length + 1; i++) {
      for (int j = 1; j < board[0].length + 1; j++) {
        map.put(i * (board[0].length + 2) + j, board[i - 1][j - 1]);
      }
    }
    return map;
  }

  public static int sum(Map<Integer, Integer> map, int[][] board, int r,
                        int c) {
    int row = board.length + 2, col = board[0].length + 2, sum = 0;
    sum += map.get((r + 1) * col + (c)) + map.get((r)*col + (c)) +
           map.get((r)*col + (c + 1)) + map.get((r + 2) * col + (c + 2)) +
           map.get((r + 1) * col + (c + 2)) + map.get((r)*col + (c + 2)) +
           map.get((r + 2) * col + (c + 1)) + map.get((r + 2) * col + (c));

    return sum;
  }

  public static void gameOfLife(int[][] board) {
    Map<Integer, Integer> map = new HashMap<Integer, Integer>();
    map = store(board);
    int r = board.length, c = board[0].length;
    /*
    for(int i=0;i<r+2;i++){
        for(int j=0;j<c+2;j++){
            System.out.println(map.get(i*(c+2)+j));
        }
    }
    */
    int[][] num = new int[r][c];
    for (int i = 0; i < r; i++) {
      for (int j = 0; j < c; j++) {
        int sum = sum(map, board, i, j);
        if (board[i][j] == 1) {
          if (2 > sum || sum > 3) {
            num[i][j] = 0;
          } else {
            num[i][j] = board[i][j];
          }
        } else {
          if (sum == 3) {
            num[i][j] = 1;
          } else {
            num[i][j] = board[i][j];
          }
        }
      }
    }
    for (int k = 0; k < r; k++) {
      board[k] = num[k].clone();
    }
  }

  public static void main(String[] args) {

    int[][] board = {{0, 1, 0}, {0, 0, 1}, {1, 1, 1}, {0, 0, 0}};
    gameOfLife(board);

    for (int i = 0; i < board.length; i++) {
      for (int j = 0; j < board[0].length; j++) {
        System.out.println(board[i][j]);
      }
    }
  }
}
