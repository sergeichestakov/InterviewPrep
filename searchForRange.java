// Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.
// Your algorithm's runtime complexity must be in the order of O(log n).
// If the target is not found in the array, return [-1, -1].

class Solution {
    public int[] searchRange(int[] nums, int target) {
		//Find first occurance of target with binary search
        int index = binarySearch(nums, target, 0, nums.length - 1);
        if(index == -1){ //Not found
            return new int[]{-1, -1};
        }
        //Expand out to find the range
        int start = index;
        int end = index;
        while(start > 0 && nums[start - 1] == target){
            start -= 1;
        }
        while(end < nums.length - 1 && nums[end + 1] == target){
            end += 1;
        }
        return new int[]{start, end};
    }
    
    private int binarySearch(int[] nums, int target, int left, int right){
        if (right >= left){
            int mid = left + (right - left) / 2;
            if(nums[mid] == target){ //Found
                return mid;
            }
            if(nums[mid] < target){ //Check upper half
                return binarySearch(nums, target, mid + 1, right);
            } else { //Check lower half
                return binarySearch(nums, target, left, mid - 1);
            }
        } else { //Not Found
            return -1;
        }
    }
}
