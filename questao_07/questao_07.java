import java.util.ArrayList;
import java.util.List;

class Professor {
    private String nome;
    private List<Escola> escolas;

    public Professor(String nome) {
        this.nome = nome;
        this.escolas = new ArrayList<>();
    }

    public String getNome() {
        return nome;
    }

    public void adicionarEscola(Escola escola) {
        escolas.add(escola);
        escola.adicionarProfessor(this);
    }

    public void listarEscolas() {
        System.out.printf("Professor %s leciona nas escolas: ", nome);
        for (Escola escola : escolas) {
            System.out.print(escola.getNome() + " ");
        }
        System.out.println();
    }
}

class Escola {
    private String nome;
    private List<Professor> professores;

    public Escola(String nome) {
        this.nome = nome;
        this.professores = new ArrayList<>();
    }

    public String getNome() {
        return nome;
    }

    public void adicionarProfessor(Professor professor) {
        professores.add(professor);
    }

    public void listarProfessores() {
        System.out.printf("Escola %s tem os professores: ", nome);
        for (Professor professor : professores) {
            System.out.print(professor.getNome() + " ");
        }
        System.out.println();
    }
}

public class questao_07 {
    public static void main(String[] args) {
        Escola escola1 = new Escola("Escola A");
        Escola escola2 = new Escola("Escola B");

        Professor professor1 = new Professor("Rodrigo");
        Professor professor2 = new Professor("Luan");

        professor1.adicionarEscola(escola1);
        professor1.adicionarEscola(escola2);
        professor2.adicionarEscola(escola1);

        professor1.listarEscolas();
        professor2.listarEscolas();

        escola1.listarProfessores();
        escola2.listarProfessores();
    }
}
