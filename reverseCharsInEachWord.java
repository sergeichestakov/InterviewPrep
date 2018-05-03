//Given a string, you need to reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.
class Solution {
    public String reverseWords(String s) {
        if(s.length() <= 1){return s;}
        StringBuilder ret = new StringBuilder();
        String[] words = s.split(" ");
        for(String word : words){
            ret.append(reverse(word) + " ");
        }
        return ret.toString().trim();
    }
    private String reverse(String word){
        String revWord = "";
        for(int i = word.length() - 1; i >= 0; i--){
            revWord += word.charAt(i);
        }
        return revWord;
    }
}
