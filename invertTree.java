/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 *
 * Invert a binary tree.
 */
class Solution {
    public TreeNode invertTree(TreeNode root) {
        if(root == null){ return root; }
        TreeNode left = root.left;
        TreeNode right = root.right;
        if(left != null || right != null){
            root.left = invertTree(right);
            root.right = invertTree(left);
        }
        return root;
    }
}
