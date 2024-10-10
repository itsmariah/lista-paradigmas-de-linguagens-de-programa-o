public class questao_13 {
    public static long fatorial(int n) {
        if (n < 0) {
            throw new IllegalArgumentException("Fatorial não é definido para números negativos.");
        }
        if (n == 0 || n == 1) {
            return 1;
        }
        return n * fatorial(n - 1);
    }

    public static void main(String[] args) {
        int numero = 5;
        long resultado = questao_13.fatorial(numero);
        System.out.printf("O fatorial de %d é %d.%n", numero, resultado);
    }
}
