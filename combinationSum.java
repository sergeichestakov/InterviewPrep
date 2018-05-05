// Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), 
// Find all unique combinations in candidates where the candidate numbers sums to target.
// The same repeated number may be chosen from candidates unlimited number of time

import java.util.*;

class Solution {
    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        List<List<Integer>> ret = new ArrayList<>();
        Arrays.sort(candidates);
        generateCombs(ret, new ArrayList<>(), candidates, target, 0);
        return ret;
    }
    
    private void generateCombs(List<List<Integer>> ret, List<Integer> temp, int[] nums, int remain, int start){
        if(remain < 0){return;} //Backtrack
        else if(remain == 0){
            ret.add(new ArrayList<>(temp));
        } else { //Try every element as many times as possible
            for(int i = start; i < nums.length; i++){
                temp.add(nums[i]);
                generateCombs(ret, temp, nums, remain - nums[i], i);
                temp.remove(temp.size() - 1);
            }
        }
        
    }
}
