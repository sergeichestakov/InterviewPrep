/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 *
 * We are given the head node root of a binary tree, where additionally every node's value is either a 0 or a 1.
 * Return the same tree where every subtree (of the given tree) not containing a 1 has been removed.
 */

class Solution {
    public TreeNode pruneTree(TreeNode root) {
        if(!containsOne(root)){return null;} //No 1's in entire tree
        if(!containsOne(root.left)){root.left = null;} //Recursively check chilren
        if(!containsOne(root.right)){root.right = null;}
        pruneTree(root.left);
        pruneTree(root.right);
        return root;
    }
    
    public boolean containsOne(TreeNode node){
        if(node == null){return false;}
        if(node.val == 1){return true;}
        return containsOne(node.left) || containsOne(node.right);
    }
}
