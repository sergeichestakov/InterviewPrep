/**
 * Definition for an interval.
 * public class Interval {
 *     int start;
 *     int end;
 *     Interval() { start = 0; end = 0; }
 *     Interval(int s, int e) { start = s; end = e; }
 * }
 *
 * Given a collection of intervals, merge all overlapping intervals.
 */
import java.util.Collections;

class Solution {
    public List<Interval> merge(List<Interval> intervals) {
        if(intervals.size() <= 1){return intervals;}
        //Sort by starting interval
        Collections.sort(intervals, new Comparator<Interval>() {
        @Override public int compare(Interval first, Interval second) {
            return first.start - second.start; // Ascending
            }
        });       
        //Build the array list by checking for overlap and taking largest end
        List<Interval> ret = new ArrayList<Interval>();
        ret.add(intervals.get(0));
        for(int index = 0; index < intervals.size(); index++){
            Interval curr = ret.get(ret.size() - 1); //Last one
            Interval next = intervals.get(index);
            
            if(next.start <= curr.end){
                curr.end = Math.max(curr.end, next.end);
            } else {
                ret.add(next);
            }
        }
        return ret;
    }
}
