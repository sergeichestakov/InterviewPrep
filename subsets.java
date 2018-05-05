// Given a set of distinct integers, nums, return all possible subsets (the power set).

import java.util.*;

class Solution {
    public List<List<Integer>> subsets(int[] nums) {
        List<List<Integer>> ret = new ArrayList<>();
        Arrays.sort(nums);
        generate(ret, new ArrayList<>(), nums, 0);
        return ret;
    }
    
    private void generate(List<List<Integer>> ret, List<Integer> temp, int[] nums, int start){
        ret.add(new ArrayList<>(temp));
        for(int i = start; i < nums.length; i++){
            temp.add(nums[i]);
            generate(ret, temp, nums, i + 1);
            temp.remove(temp.size() - 1);
        }
    }
}
