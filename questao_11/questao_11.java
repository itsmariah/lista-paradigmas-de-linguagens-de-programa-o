// Classes Abstratas Crie uma classe abstrata Funcionario com um método abstrato calcularSalario. Derive classes como FuncionarioHorista e FuncionarioAssalariado que
// implementam calcularSalario de formas distintas.

abstract class Funcionario {
    public abstract double calcularSalario();

    protected abstract Object getNome();
}

class FuncionarioHorista extends Funcionario {
    private String nome;
    private int horasTrabalhadas;
    private double valorHora;

    public FuncionarioHorista(String nome, int horasTrabalhadas, double valorHora) {
        this.nome = nome;
        this.horasTrabalhadas = horasTrabalhadas;
        this.valorHora = valorHora;
    }

    @Override
    public double calcularSalario() {
        return horasTrabalhadas * valorHora;
    }

    public String getNome() {
        return nome;
    }
}

class FuncionarioAssalariado extends Funcionario {
    private String nome;
    private double salarioMensal;

    public FuncionarioAssalariado(String nome, double salarioMensal) {
        this.nome = nome;
        this.salarioMensal = salarioMensal;
    }

    @Override
    public double calcularSalario() {
        return salarioMensal;
    }

    public String getNome() {
        return nome;
    }
}

public class questao_11 {
    public static void main(String[] args) {
        Funcionario funcionario1 = new FuncionarioHorista("Junior", 160, 20);
        Funcionario funcionario2 = new FuncionarioAssalariado("Vanessa", 3000);

        System.out.printf("Salário de %s: R$ %.2f%n", funcionario1.getNome(), funcionario1.calcularSalario());
        System.out.printf("Salário de %s: R$ %.2f%n", funcionario2.getNome(), funcionario2.calcularSalario());
    }
}
