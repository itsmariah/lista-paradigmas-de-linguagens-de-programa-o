// Sobrecarga de Métodos (Java) / Métodos com Nomes Diferentes (Python, Go): Implemente uma classe Calculadora com métodos somar que aceita diferentes números
// de parâmetros (dois ou três números). Em Golang, use funções com nomes diferentes para diferentes quantidades de parâmetros.

public class questao_10 {
    
    public int somar(int a, int b) {
        return a + b;
    }

    
    public int somar(int a, int b, int c) {
        return a + b + c;
    }

    public static void main(String[] args) {
        questao_10 calc = new questao_10();

        int resultado1 = calc.somar(10, 20);
        int resultado2 = calc.somar(10, 20, 30);

        System.out.println("Resultado da soma de dois números: " + resultado1);
        System.out.println("Resultado da soma de três números: " + resultado2);
    }
}
