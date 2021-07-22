import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        System.out.print("Пожалуйста, введите число N: ");
        int N = in.nextInt();
//        int[] A = new int[N];
        int amount0 = 0, amount1 = 0;
        for (int i = 0; i < N; i++) {
            System.out.print("Пожалуйста, введите число (1 или 0) для обозначения положения монеты: ");
            int side = in.nextInt();
            if (side == 0) {
//                A[i] = side;
                amount0++;
            } else if (side == 1) {
//                A[i] = side;
                amount1++;
            } else {
                System.out.println("Введены некорректные данные. Пожалуйста, попробуйте снова");
                i--;
            }
        }
        int min = Math.min(amount0, amount1);
//        int min = solution(A, N);
        System.out.println("Минимальное число монет, которые должны быть перевернуты: " + min);
    }

//  ---  adding another function seemed senseless  ---
//  ---  task could be resolved with two functions, but in my realization it would only cause extra resource loss  ---
//
//    public static int solution(int[] A, int N) {
//        int min, amount0, amount1;
//        for(int i = 0; i < N; i++){
//            if (A[i] == 0)
//        }
//        min = 0;
//        return min;
//    }
}
