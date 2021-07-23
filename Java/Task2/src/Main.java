import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        System.out.print("Пожалуйста, введите текст: ");
        String S = in.nextLine();
        char[] SChars = S.toCharArray();
        int words = 0, prevWords = 0;
        boolean isEmpty = true;
        for (char ch : SChars) {
            if (ch != ' ') {
                if ((ch == '.' || ch == '?' || ch == '!') && !isEmpty) {
                    isEmpty = true;
                    words = Math.max(words, prevWords+1);
                    prevWords = 0;
                }
                else {
                    isEmpty = false;
                }
            } else if (!isEmpty) {
                isEmpty = true;
                prevWords++;
            }
        }
        System.out.println(words);
    }
}