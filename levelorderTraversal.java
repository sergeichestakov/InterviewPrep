/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 *
 * Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).
 */
import java.util.*;

class Solution {
    public List<List<Integer>> levelOrder(TreeNode root) {      
        List<List<Integer>> ret = new ArrayList<>();
        if(root == null){
            return ret;
        }
        
        Queue<TreeNode> q = new LinkedList<>();
        q.add(root);
        int level = 0;
        
        while(true){
            int nodeCount = q.size();
            if(nodeCount == 0){
                break;
            }
            
            while(nodeCount > 0) {
                TreeNode node = q.poll();
                if(level >= ret.size()){
                    ret.add(new ArrayList<Integer>());
                }
                ret.get(level).add(node.val);
                if(node.left != null){
                    q.add(node.left);
                }
                if(node.right != null){
                    q.add(node.right);
                }
                nodeCount--;
            }
            level++;
        }
        return ret;
    }
}
