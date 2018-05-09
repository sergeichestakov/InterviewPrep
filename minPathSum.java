// Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.
// Note: You can only move either down or right at any point in time.
class Solution {
   public int minPathSum(int[][] grid) {
        //Build a grid up from scratch, take the min of upper and left at each point
        int rows = grid.length;
        int cols = grid[0].length;
        int[][] totalPath = new int[rows][cols];

        //Build the path grid starting from first one
        totalPath[0][0] = grid[0][0];
        for(int row = 0; row < rows; row++){
            for(int col = 0; col < cols; col++){
                //Each elem is the min of the left and upper + itself
                if(row == 0 && col == 0){continue;}
                int upper = Integer.MAX_VALUE;
                int left = Integer.MAX_VALUE;
                if(row != 0){
                    upper = totalPath[row - 1][col];
                }
                if(col != 0){
                    left = totalPath[row][col - 1];
                }
                totalPath[row][col] = Math.min(upper, left) + grid[row][col];
            }
        }
       	//Return the last element to find the best path 
        return totalPath[rows - 1][cols - 1];
    }
}
