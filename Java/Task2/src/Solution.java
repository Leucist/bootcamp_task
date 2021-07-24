public class Solution {
    public static void main(String[] args) {
        if(args.length > 0) {
            int words = solution(args[0]);
            System.out.println(words);
        }
        else {
            throw new IllegalArgumentException("Argument is reqiured('S' string)");
        }
    }

    public static int solution(String S) {
        char[] SChars = S.toCharArray();
        int words = 0, prevWords = 0;
        boolean isEmpty = true;
        for (char ch : SChars) {
            if (ch != ' ') {
                if ((ch == '.' || ch == '?' || ch == '!') && !isEmpty) {
                    isEmpty = true;
                    words = Math.max(words, prevWords + 1);
                    prevWords = 0;
                } else {
                    isEmpty = false;
                }
            } else if (!isEmpty) {
                isEmpty = true;
                prevWords++;
            }
        }
        return words;
    }
}
