import java.util.LinkedList;

public class Solution {
    public static void main(String[] args){
        if (args.length > 0) {
            int number = solution(Integer.parseInt(args[0]));
            System.out.println(number);
        }
        else {
            throw new IllegalArgumentException("Argument is required('A' number)!");
        }
    }
    public static int solution(int A){
        String S = String.valueOf(A);
        char[] SChars = S.toCharArray();
        int l = SChars.length - 1;

        LinkedList<String> newNumber = new LinkedList<>();

        for (int i = 0; i <= l; i++) {
            newNumber.add(String.valueOf(SChars[i]));
        }
        int m = 0;
        for (int i = 0; i <= l; i++) {
            if (i % 2 == 1) {
                newNumber.add(i, String.valueOf(SChars[l - m]));
                m++;
            }
        }
        int brandNewNumber = 0;
        for (int i = 0; i <= l; i++) {
            brandNewNumber *= 10;
            brandNewNumber += Integer.parseInt(newNumber.get(i));
        }
        return brandNewNumber;
    }
}
