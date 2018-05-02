// Given an input string, reverse the string word by word.
import java.util.*;

public class Solution {
    public String reverseWords(String s) {
        String[] words = s.trim().split("\\s+");
        if(words.length == 0){return "";}
        StringBuilder str = new StringBuilder();
        for(String word : words){
            str.insert(0, word + " ");
        }
        return str.toString().trim();
    }
}
