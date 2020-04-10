package com.company;

import javax.swing.tree.TreeNode;
import java.util.Enumeration;

public class Main {
    public static void createBinTree(TreeNode root){
        TreeNode p=new TreeNode() {
            @Override
            public TreeNode getChildAt(int childIndex) {
                return null;
            }

            @Override
            public int getChildCount() {
                return 0;
            }

            @Override
            public TreeNode getParent() {
                return null;
            }

            @Override
            public int getIndex(TreeNode node) {
                return 0;
            }

            @Override
            public boolean getAllowsChildren() {
                return false;
            }

            @Override
            public boolean isLeaf() {
                return false;
            }

            @Override
            public Enumeration<? extends TreeNode> children() {
                return null;
            }
        }
        TreeNode newNodeB = new TreeNode(2,"B");
        TreeNode newNodeC = new TreeNode(3,"C");
        TreeNode newNodeD = new TreeNode(4,"D");
        TreeNode newNodeE = new TreeNode(5,"E");
        TreeNode newNodeF = new TreeNode(6,"F");
        root.leftChild=newNodeB;
        root.rightChild=newNodeC;
        root.leftChild.leftChild=newNodeD;
        root.leftChild.rightChild=newNodeE;
        root.rightChild.rightChild=newNodeF;
    }


    public static void main(String[] args) {





    }
}
