import java.util.ArrayList;
import java.util.List;

class Empregado {
    private String nome;
    private String cargo;
    private double salario;

    public Empregado(String nome, String cargo, double salario) {
        this.nome = nome;
        this.cargo = cargo;
        this.salario = salario;
    }

    public String getNome() {
        return nome;
    }

    public String getCargo() {
        return cargo;
    }

    public double getSalario() {
        return salario;
    }
}

class Empresa {
    private String nome;
    private List<Empregado> empregados;

    public Empresa(String nome) {
        this.nome = nome;
        this.empregados = new ArrayList<>();
    }

    public void adicionarEmpregado(Empregado empregado) {
        empregados.add(empregado);
    }

    public void listarEmpregados() {
        System.out.printf("Empregados da empresa %s:%n", nome);
        for (Empregado empregado : empregados) {
            System.out.printf("Nome: %s, Cargo: %s, Salário: %.2f%n", empregado.getNome(), empregado.getCargo(), empregado.getSalario());
        }
    }

    public static void main(String[] args) {
        Empresa empresa = new Empresa("Tech Solutions");

        Empregado emp1 = new Empregado("Isadora", "Desenvolvedora", 5000.00);
        Empregado emp2 = new Empregado("Diogo", "Gerente", 8000.00);
        Empregado emp3 = new Empregado("Carolina", "Analista", 6000.00);

        empresa.adicionarEmpregado(emp1);
        empresa.adicionarEmpregado(emp2);
        empresa.adicionarEmpregado(emp3);

        empresa.listarEmpregados();
    }
}
